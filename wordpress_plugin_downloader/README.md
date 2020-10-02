## Wordpress Plugin Downloader
Two simple scripts to scrape all popular Wordpress plugins's information, download and extract them.

## Requirements

- `BeautifulSoup`
- `requests`

```
pip install BeautifulSoup requests
```

- `axel`, on Ubuntu install with

```
sudo apt install axel
```

## How to
Run the `wordpress_plugin.py` will crawl and save information to `popular.csv` file.

```
python wordpress_plugin.py
```

Put list of urls to file `downloader.py` into variable `URLS` (see sample) to download plugins

```
python downloader.py
```
