# Wordpress Plugin Downloader

Two simple scripts to scrape all popular Wordpress plugins' information, download and extract them.

## Requirements

- `BeautifulSoup`
- `requests`

```bash
pip install BeautifulSoup requests
```

- `axel`, on Ubuntu install with

```bash
sudo apt install axel
```

## How to

Run the `wordpress_plugin.py` script to crawl and save information to `popular.csv` file.

```bash
python wordpress_plugin.py
```

Put list of urls to file `downloader.py` into variable `URLS` (see sample) to download plugins

```bash
python downloader.py
```
