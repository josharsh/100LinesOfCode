"""A simple URL shortener service using Flask. This application maps short
URLs to their corresponding long URLs and redirects users accordingly."""
import threading
import random
import json
from flask import Flask, redirect

app = Flask(__name__)

try:
    with open('data.json', 'r', encoding='utf-8') as json_file:
        short_to_long = json.load(json_file)
        print("Found existing data.json. Loaded short-to-long URL mappings.")
except (FileNotFoundError, json.JSONDecodeError):
    print("data.json not found or invalid. Starting with an empty mapping.")
    short_to_long = {}

@app.route('/<short_url>')
def redirect_to_url(short_url):
    """Redirects to the original long URL based on the provided short URL."""
    long_url = short_to_long.get(short_url)
    if long_url:
        if long_url.startswith("http://") or long_url.startswith("https://"):
            print(f"Redirecting short URL: {short_url} to long URL: {long_url}")
            return redirect(long_url)
        else:
            print(f"Redirecting short URL: {short_url} to long URL: {long_url}")
            return redirect(f"https://{long_url}")
    else:
        return "Short URL not found", 404

@app.route('/shorten/<long_url>')
def shorten_url(long_url):
    """Generates a short URL for the given long URL and stores the mapping."""
    short_url = ''.join(random.choices
            ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
    short_to_long[short_url] = long_url
    print(f"Generated short URL: {short_url} for long URL: {long_url}")
    save_mappings()
    return f"Short URL: {short_url}"

# @app.route('/save')
def save_mappings():
    """Saves the current short-to-long URL mappings to a file."""
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(short_to_long, f)
    return "Mappings saved successfully"

def threaded_run():
    """Runs the Flask application in a separate thread to allow for concurrent execution."""
    def _run_threaded():
        app.run(debug=True, port=5000, host='0.0.0.0', use_reloader=False)
    return _run_threaded

if __name__ == '__main__':
    run_thread = threading.Thread(target=threaded_run())
    run_thread.start()
