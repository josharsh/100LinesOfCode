import queue, threading, time, uuid, random

# ---------- system state ----------
jobs = queue.Queue()
completed = []
dlq = []
metrics = {"done": 0, "failed": 0}

# ---------- logging ----------
def log(trace, event, msg=""):
    print(f"{trace:8} | {event:10} | {msg}")

# ---------- job behavior ----------
def handle(job):
    if job["type"] == "send_email":
        time.sleep(0.05)
    elif job["type"] == "resize_image":
        time.sleep(0.15)
    elif job["type"] == "charge_card":
        if random.random() < 0.4:
            raise Exception("payment timeout")

# ---------- worker ----------
def worker():
    while True:
        job = jobs.get()
        trace = job["trace"]
        try:
            handle(job)
            job["duration"] = time.time() - job["start"]
            completed.append(job)
            metrics["done"] += 1
        except Exception:
            job["retries"] += 1
            if job["retries"] > 3:
                job["duration"] = time.time() - job["start"]
                dlq.append(job)
                metrics["failed"] += 1
            else:
                time.sleep(2 ** job["retries"])
                jobs.put(job)
        jobs.task_done()

# ---------- monitor ----------
def monitor():
    while True:
        print(
            f"[MONITOR] queue={jobs.qsize()} "
            f"done={metrics['done']} dlq={len(dlq)}"
        )
        time.sleep(1)

# ---------- submit ----------
def submit(job_type):
    jobs.put({
        "id": str(uuid.uuid4()),
        "type": job_type,
        "retries": 0,
        "trace": str(uuid.uuid4())[:8],
        "start": time.time(),
    })

# ---------- bootstrap ----------
for _ in range(4):
    threading.Thread(target=worker, daemon=True).start()

threading.Thread(target=monitor, daemon=True).start()

JOB_TYPES = ["send_email", "resize_image", "charge_card"]
for _ in range(1000): # Scale this number as needed
    submit(random.choice(JOB_TYPES))

jobs.join()

# ---------- visualization ----------
print("\n=== RESULTS ===")
total = metrics["done"] + metrics["failed"]
print(f"Total jobs: {total}")
print(f"Success   : {metrics['done']}")
print(f"DLQ       : {metrics['failed']}")

print("\nSuccess vs DLQ")
print("SUCCESS |", "#" * (metrics["done"] // 20))
print("DLQ     |", "#" * (metrics["failed"] // 20))

buckets = {"<0.5s": 0, "0.5-2s": 0, ">2s": 0}
for j in completed + dlq:
    d = j["duration"]
    if d < 0.5:
        buckets["<0.5s"] += 1
    elif d < 2:
        buckets["0.5-2s"] += 1
    else:
        buckets[">2s"] += 1

print("\nLatency distribution")
for k, v in buckets.items():
    print(f"{k:7} | {'#' * (v // 20)}")
