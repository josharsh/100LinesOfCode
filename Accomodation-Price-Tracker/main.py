from database import DatabaseHandler
from scrapers import FusionStudentsScraper, MezzinoScraper

if __name__ == "__main__":
    db = DatabaseHandler("prices.db")
    for s in [MezzinoScraper("Belgrave View", "https://www.mezzino.com/property/belgrave-view/", "https://www.mezzino.com/wp-json/room-filter/v1/rooms?property_id=19606&display_year=current_year", db), FusionStudentsScraper("Fusion Students Birmingham", "https://www.fusionstudents.co.uk/property/birmingham/", db)]: s.run()
    print("[+] All scrapers finished execution.")