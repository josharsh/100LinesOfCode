import sqlite3

class DatabaseHandler:
    def __init__(self, db_name):
        self.db_name = db_name
        with sqlite3.connect(self.db_name) as conn:
            conn.execute("CREATE TABLE IF NOT EXISTS rooms (room_id TEXT PRIMARY KEY, name TEXT, provider TEXT)")
            conn.execute("CREATE TABLE IF NOT EXISTS prices (id INTEGER PRIMARY KEY AUTOINCREMENT, room_id TEXT, price REAL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)")

    def get_latest_price(self, room_id, conn):
        res = conn.execute("SELECT price FROM prices WHERE room_id = ? ORDER BY timestamp DESC LIMIT 1", (room_id,)).fetchone()
        return res[0] if res else None

    def save_prices(self, scraped_rooms, provider_name, property_name):
        drops, raises = [], []
        with sqlite3.connect(self.db_name) as conn:
            for item in scraped_rooms:
                clean_name = item["name"].split(property_name)[-1].strip(" -:") if property_name in item["name"] else item["name"]
                comp_id = f"{provider_name.lower().replace(' ', '')}_{item['id']}"
                conn.execute("INSERT OR REPLACE INTO rooms VALUES (?, ?, ?)", (comp_id, clean_name, provider_name))
                prev = self.get_latest_price(comp_id, conn)
                if prev is not None:
                    if item["price"] < prev:
                        drops.append({"name": clean_name, "old_price": prev, "new_price": item["price"], "saving": prev - item["price"]})
                    elif item["price"] > prev:
                        raises.append({"name": clean_name, "old_price": prev, "new_price": item["price"], "increase": item["price"] - prev})
                conn.execute("INSERT INTO prices (room_id, price) VALUES (?, ?)", (comp_id, item["price"]))
        return drops, raises