# Subnet Pinger
 My own implementation of an active-device finder, because pinging your Subnet with a broadcast address takes ages AND not all devices might respond.
 It launches multiple processes for each ping to speed up the process.
 Watch out, you might DOS your own subnet! I'm not responsible for damages if so, consider yourselves warned! :D

# Usage
./pinger.sh [-n netmask -i IP] [-f]

 -n Allows you to specify a custom netmask in the dotted decimal convention.
 
 -i Allows you to specify a custom ip in the dotted decimal convention.
 
 -f Enables file logging (saves found devices in a text file).
 

#### Example:
./pinger.sh -n 255.255.255.0 -i 192.168.2.1


# Files
IPTools.sh -> contains the function to convert from quadruple-dotted-decimal to integer
pinger.sh -> contains the actual code to ping
