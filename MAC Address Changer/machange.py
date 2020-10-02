
def mac_random():
    """Generate a random MAC address taking the first 3 pairs from
Cisco and Dell defined hardware, and generate the 3 last pairs randomly"""
    cisco = ["00", "40", "96"]
    dell = ["00", "14", "22"]
    mac_address = choice([cisco, dell])
    for i in range(3):
        one = choice(str(randint(0, 9)))
        two = choice(str(randint(0, 9)))
        three = (str(one + two))
        mac_address.append(three)
    return ":".join(mac_address)


def change_mac(interface, new_mac):
    """Use Linux commands to change the mac"""
    subprocess.call(["ifconfig " + str(interface) + " down"], shell=True)
    subprocess.call(["ifconfig " + str(interface) +
                     " hw ether " + str(new_mac) + " "], shell=True)
    subprocess.call(["ifconfig " + str(interface) + " up"], shell=True)


def CurrentMac():
    """Check the current MAC, taking it from the ifconfig + interface output
and taking only the MAC with Regular Expresions in this case it takes any alphanumeric character"""
    output = subprocess.check_output(["ifconfig " +
                                      args.interface], shell=True)
    current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output))
return current_mac