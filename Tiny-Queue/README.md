# Tiny Queue

A lightweight, production-ready job queue system with worker threads, automatic retries, dead letter queue (DLQ), and real-time monitoring - all in exactly 100 lines of Python!

## Description

Tiny Queue demonstrates how to build a resilient background job processing system with minimal code. It includes:

- **Multi-threaded Workers**: Concurrent job processing with configurable worker count
- **Automatic Retries**: Exponential backoff retry mechanism for failed jobs
- **Dead Letter Queue (DLQ)**: Failed jobs after max retries are moved to DLQ for inspection
- **Real-time Monitoring**: Live dashboard showing queue size, completed jobs, and failures
- **Performance Metrics**: Visual latency distribution and success rate statistics

Perfect for understanding concurrency, job queues, and error handling patterns in Python!

## Features

✨ **Key Highlights**:
- 4 worker threads processing jobs concurrently
- Automatic retry with exponential backoff (2^retries seconds)
- Dead letter queue for permanently failed jobs
- Real-time metrics tracking (success/failure rates)
- Latency distribution analysis
- Visual ASCII-based result charts

## Installation

No external dependencies required! Uses only Python standard library:

```bash
# Clone the repository
git clone https://github.com/josharsh/100LinesOfCode.git
cd 100LinesOfCode/Tiny-Queue

# Run the project (Python 3.6+)
python main.py
```

## Usage

### Basic Execution

Simply run the script:

```bash
python main.py
```

### Example Output

```
[MONITOR] queue=987 done=12 dlq=0
[MONITOR] queue=854 done=134 dlq=2
[MONITOR] queue=721 done=256 dlq=5
...

=== RESULTS ===
Total jobs: 1000
Success   : 856
DLQ       : 144

Success vs DLQ
SUCCESS | ##########################################
DLQ     | #######

Latency distribution
<0.5s   | ############################
0.5-2s  | ##########
>2s     | ####
```

### Customization

Modify the code to fit your needs:

```python
# Change number of workers (line 68)
for _ in range(8):  # 8 workers instead of 4
    threading.Thread(target=worker, daemon=True).start()

# Adjust job volume (line 73)
for _ in range(5000):  # Process 5000 jobs
    submit(random.choice(JOB_TYPES))

# Add custom job types (line 15-22)
def handle(job):
    if job["type"] == "your_custom_job":
        # Your job logic here
        time.sleep(0.1)
```

## How It Works

1. **Job Submission**: Jobs are added to the queue with unique IDs and trace identifiers
2. **Worker Processing**: Multiple workers pull jobs from the queue and execute them
3. **Error Handling**: Failed jobs are retried with exponential backoff (up to 3 retries)
4. **DLQ Transfer**: Jobs exceeding retry limit are moved to the Dead Letter Queue
5. **Monitoring**: Background thread displays real-time queue statistics every second
6. **Results**: Final visualization shows success rates and latency distribution

## Job Types

The demo includes three job types:

- **send_email**: Fast job (50ms) - always succeeds
- **resize_image**: Medium job (150ms) - always succeeds  
- **charge_card**: Fast job with 40% failure rate - demonstrates retry logic

## Technologies

- **Language**: Python 3.6+
- **Core Libraries**: 
  - `queue` - Thread-safe queue implementation
  - `threading` - Concurrent worker threads
  - `time` - Timing and delays
  - `uuid` - Unique job identifiers
  - `random` - Job type selection and failure simulation

## Use Cases

This pattern is useful for:

- Background job processing (emails, notifications)
- Image/video processing pipelines
- Payment processing with retries
- Data ingestion and ETL tasks
- Webhook delivery systems
- Batch processing workflows

## Learning Outcomes

By studying this code, you'll learn:

- Thread-safe queue operations in Python
- Worker thread pool patterns
- Exponential backoff retry strategies
- Dead letter queue implementation
- Real-time monitoring and metrics collection
- Concurrent programming best practices

## Code Structure

```
Tiny-Queue/
├── main.py          # Complete queue system (100 lines)
└── README.md        # This file
```

## Author

Contributed to [100 Lines of Code](https://github.com/josharsh/100LinesOfCode)

## License

This project is part of the 100 Lines of Code repository, licensed under the [GNU General Public License v3.0](../LICENSE).

---

⭐ If you find this helpful, please star the [100 Lines of Code repository](https://github.com/josharsh/100LinesOfCode)!
