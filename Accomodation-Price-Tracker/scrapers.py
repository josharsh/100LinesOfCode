import html, os, re, requests
from bs4 import BeautifulSoup

DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK")

class BaseScraper:
    def __init__(self, property_name, property_url, provider_name, db_handler):
        self.property_name, self.property_url = property_name, property_url
        self.provider_name, self.db_handler = provider_name, db_handler

    def send_discord_alert(self, drops, raises):
        if not DISCORD_WEBHOOK_URL:
            return print("[!] No Discord webhook configured. Skipping alert.")
        embeds = [{
            "title": f"🚨 Price Drop at {self.property_name}: {d['name']} 🚨" if is_drop else f"📈 Price Increase at {self.property_name}: {d['name']} 📈",
            "description": f"**Was:** £{d['old_price']:.2f}/wk\n**Now:** £{d['new_price']:.2f}/wk\n**{'Savings' if is_drop else 'Increase'}:** {'-' if is_drop else '+'}\n£{d['saving' if is_drop else 'increase']:.2f}/wk",
            "color": 0x2ECC71 if is_drop else 0xFF0000, "url": self.property_url
        } for is_drop, items in [(True, drops), (False, raises)] for d in items]
        try:
            requests.post(DISCORD_WEBHOOK_URL, json={"embeds": embeds}, timeout=10).raise_for_status()
            print(f"[+] Discord alert sent for {self.property_name}.")
        except Exception as e:
            print(f"[!] Failed to send Discord alert: {e}")

    def scrape(self):
        raise NotImplementedError

    def run(self):
        rooms = self.scrape()
        if not rooms:
            return print(f"[!] No rooms found for {self.property_name}. Skipping.")
        drops, raises = self.db_handler.save_prices(rooms, self.provider_name, self.property_name)
        if drops or raises:
            self.send_discord_alert(drops, raises)

class MezzinoScraper(BaseScraper):
    def __init__(self, property_name, property_url, api_url, db_handler):
        super().__init__(property_name, property_url, "Mezzino", db_handler)
        self.api_url = api_url

    def scrape(self):
        headers = {"User-Agent": "Mozilla/5.0", "Accept": "*/*", "Referer": self.property_url}
        try:
            r = requests.get(self.api_url, headers=headers, timeout=15)
            r.raise_for_status()
            rooms = []
            for item in r.json():
                if item.get("availability_this_year") != "sold-out" and item.get("lowest_rate_current_year"):
                    rooms.append({"id": str(item.get("id")), "name": html.unescape(item.get("title", f"Room {item.get('id')}")), "price": float(item["lowest_rate_current_year"])})
            return rooms
        except Exception as e:
            print(f"[!] Error fetching Mezzino API: {e}"); return []

class FusionStudentsScraper(BaseScraper):
    def __init__(self, property_name, property_url, db_handler):
        super().__init__(property_name, property_url, "Fusion Students", db_handler)

    def scrape(self):
        try:
            soup = BeautifulSoup(requests.get(self.property_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=15).text, "html.parser")
            rooms, seen = [], set()
            for b in soup.select(".room-option-info"):
                t, p = b.find("h3"), b.find("span", class_="room-option-from")
                if t and p:
                    rid = b.get("data-modalid", "").replace("room-modal-", "") or re.sub(r"\W+", "_", t.text.lower()).strip("_")
                    p_match = re.search(r"£\s*([\d\.]+)", p.text)
                    if rid not in seen and p_match:
                        seen.add(rid)
                        rooms.append({"id": rid, "name": html.unescape(t.get_text(strip=True)), "price": float(p_match.group(1))})
            return rooms
        except Exception as e:
            print(f"[!] Error scraping Fusion Students: {e}"); return []