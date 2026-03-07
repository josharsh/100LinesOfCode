# Auto-VirusTotal

Many Cybersecurity professionals often end up with several lists of possible IOC hashes on their hands.

This is a small GO CLI tool that reads a file of hashes from a text file and queries VirusTotal for their detection results to determine whether they are malicious or not. The tool prints the number of malicious, suspicious, and harmless detections for each hash.

## Features

- Reads hashes from a file (one per line)
- Queries the VirusTotal API (using your own API token)
- Prints detection statistics.


## Technologies
- Go
- VirusTotal

## Requirements

- A VirusTotal API key.

You can obtain a free API key by creating an account on VirusTotal.

Note: The free API is limited to 4 requests per minute. When using a free API key you could modify the script to add a sleep timer for optimal performance.

## Usage

An example test.txt file is provided with the hash of EICAR (commonly used in detection tests).

### Example Command

go run Auto-VirusTotal.go test.txt <API KEY>

## Disclaimer

This project is for educational and research purposes only.