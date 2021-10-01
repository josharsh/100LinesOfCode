# MAC Address Changer in Python
# The commands required to change the mac address from the terminal:
# ifconfig eth0 down (To switch off the eth0 connection)
# ifconfig eth0 hw ether "MAC ADDRESS ASSIGNED" (hw denotes Hardware)
# ifconfig eth0 up (Switch the service back on)

# A module called "subprocess" is used to execute linux(any) system commands depending on the OS.
# We use a function of module subprocess called "call" that runs the system commands in the foreground
# and waits for the command to finish before executing the next command
# Syntax = subprocess.call("COMMAND",Shell=True)

# SIOCSIFFLAGS->Operation not permitted : Run the command as Root
# make sure to run the program as root

# optparse helps in passing arguments by taking input from user
# !/usr/bin/env python3    -> sha-bang
import subprocess
import optparse
import re


def get_arguments():
	# parser object: knows everything about the arguments and parsing them ie entity that handles user input
	# parser is a variable that holds optparse.OptionParser() class ie an instance is created
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's MAC address")
	parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
	(option, arguments) = parser.parse_args()
	if not option.interface:
		parser.error("Please specify an interface and use --help for more information")
	elif not option.new_mac:
		parser.error("Please specify a new_mac and use --help for more information")
	return option


# options : value of input whose destination is given and arguments are for -i and -- interface etc.

def change_mac(interface, new_mac):
	print("# Changing the MAC Address of " + interface + "to" + new_mac)
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig", interface])
	print(ifconfig_result)

	# Extracting MAC Address using REGEX
	mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
	if mac_address_search_result:
		return mac_address_search_result.group(0)
	else:
		print("Couldn't read MAC address")


# subprocess.call("ifconfig "+interface+" down", shell=True) is not safe as interface allows
# any command to be given by the user which makes the tool vulnerable like enter 2 commands
# (using ; that marks end of command) , Hence we use the second syntax of Subprocess

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))
change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
	print("MAC Address was successfully changed to " + current_mac)
else:
	print("MAC Address did not change")