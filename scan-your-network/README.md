# Scan Your Network by Net-Scan
## About the tool
Purpose of this tool is to scan your local network and give back the number of machines connected to it, the program is designed to be less than 100 lines of code. It is a CLI based tool that shows machines IP addresses along with their mac addresses. It can scan a specific IP or the range of your network. This information can be used for security purpose, scanning purpose and others.

### Requirements
You have to install the scapy library from python.
 ```
 $ pip install scapy
 ```

### How to scan
For scanning a specific IP
```
$ python netscan.py -t [IP ADDRESS]
```
For scanning the range, for eg: ***192.168.0.0/24***
```
$ python netscan.py -t [IP NETWORK]/[CIDR]
```

The tool has the help command to know more, -h or --help.
```
$ python netscan.py -h 
```

##### Author - Deepak Kumar Giri