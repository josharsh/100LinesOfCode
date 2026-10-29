# Birmingham Student Accommodation Price Tracker

A student accommodation price monitoring system I made in Python. It tracks pricing changes across accommodation providers (currently mezzino Belgrave View and Fusion Students) in Birmingham, adds data into an SQLite database, and sends an alert through Discord when prices drop or raise. This can be extended to more providers because of the modular design of the scripts.

---

## Key Features

- Object-Oriented Architecture: Designed using OOP, its easy to plug in new accommodation providers without duplicate code.
- Multi-Provider Scraping:
  - Mezzino (Belgrave View): REST API JSON extraction.
  - Fusion Students Birmingham: HTML DOM parsing using BeautifulSoup4 and regex for room options.
- Relational SQLite Database: Uses contextual SQL transactions to maintain rooms and prices tables, logs price points.
- Discord Alerts: Sends embedded webhooks for price drops (green) and price increases (red).
- CI/CD Integration: Runs on a scheduled GitHub Actions workflow (scraper.yml).

---

## Architecture & Project Structure
```
belgrave-tracker/
├── .github/
│   └── workflows/
│       └── scraper.yml    # Scheduled GitHub Actions cron job
├── database.py            # DatabaseHandler class for SQLite context execution
├── scrapers.py            # BaseScraper parent class & provider child scrapers
├── main.py                # Pipeline entry point & execution orchestrator
├── prices.db              # SQLite database (persisted state)
└── requirements.txt       # Project dependencies
```
---

## Database Schema

The backend uses SQLite (prices.db) with two foreign-key linked tables:

### rooms Table
- room_id (TEXT, PRIMARY KEY): Provider key + room identifier
- name (TEXT, NOT NULL): Room category title
- provider (TEXT, NOT NULL): Accommodation provider name

### prices Table
- id (INTEGER, PRIMARY KEY AUTOINCREMENT): Surrogate key
- room_id (TEXT, FOREIGN KEY): References rooms(room_id)
- price (REAL, NOT NULL): Weekly rate in GBP
- timestamp (DATETIME, DEFAULT CURRENT_TIMESTAMP): UTC log timestamp

---

## Setup & Usage

### 1. Prerequisites
- Python 3.9+
- Virtual environment (recommended)

### 2. Installation
Clone the repository and install dependencies:
```
git clone https://github.com/JeremyM07/belgrave-tracker.git
cd belgrave-tracker
pip install -r requirements.txt
```

### 3. Environment Variables
Set your Discord Webhook URL (optional for local testing without notifications):
export 
```
DISCORD_WEBHOOK="https://discord.com/api/webhooks/YOUR/WEBHOOK/URL"
```

### 4. Running Locally
Execute the pipeline orchestration script:
```python main.py```

---

## Adding a New Accommodation Provider

To add a new provider:

1. Inherit from BaseScraper in scrapers.py:
   
```python
class NewProviderScraper(BaseScraper):
    def __init__(self, property_name, property_url, api_url, db_handler):
        super().__init__(
            property_name=property_name,
            property_url=property_url,
            provider_name="New Provider",
            db_handler=db_handler
        )
        self.api_url = api_url

    def scrape(self):
        # Fetch data and return a list of standard dicts:
        # [{"id": "unique_id", "name": "Room Name", "price": 190.00}]
        pass
```
2. Register the scraper in main.py:
```
new_scraper = NewProviderScraper(...)
scrapers = [mezzino, fusion, new_scraper]
```
