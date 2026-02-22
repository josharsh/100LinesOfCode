# URL Shortener

A simple URL shortener service using Flask. This application maps short URLs to their corresponding long URLs and redirects users accordingly.

## Features

- Create short URLs for long URLs
- Redirect users from short URLs to long URLs

## Running the Application

1. Clone the repository:

   ```bash
   git clone https://github.com/josharsh/100LinesOfCode.git
   ```

2. Navigate to the project directory:

   ```bash
   cd 100LinesOfCode/URL\ Shortener
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python main.py
   ```

5. Open your web browser and go to `http://localhost:5000` to use the URL shortener.

## Usage

- To create a short URL, access /shorten/long_url where `long_url` is the URL you want to shorten. For example:

  ```http://localhost:5000/shorten/www.example.com```

To expand a short URL, access /short_url where `short_url` is the short URL you want to expand. For example:

  ```http://localhost:5000/short/abc123```
