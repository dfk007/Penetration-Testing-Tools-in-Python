# Packets flow from source mac to the destination mac
# Anonymity, Impersonate, Bypass filters

# Subprocess Management
# Subprocess allows us to execute system commands. Commands depend on the OS you're on.

# optparse allows us to take input as args from user, parse them and process in our code.

# subprocess.call("COMMAND", shell=True)

import subprocess
import optparse


# subprocess.call("ifconfig " + interface + " down", shell=True)
# print(interface + " down.")
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# print("Changing MAC")
# subprocess.call("ifconfig " + interface + " up", shell=True)
# print(interface + " up.")


def get_arguments():
    # creating a parser object -An entity that handles user input
    # parser var - is an instance of OptionParser class

    parser = optparse.OptionParser()  # OptionParser is a class as it starts with a capital O_P

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")

    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    (options, arguments) = parser.parse_args()

    if not options.interface:
        # Code to handle error
        parser.error("[-] Please specify an interface, use --help for more info")

    if not options.new_mac:
        # Code to handle error
        parser.error("[-] Please specify a MAC, use --help for more info")

    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC Address for " + interface + " to " + new_mac)
    # Secure version of subprocess call - Input is restricted to fixed params.
    subprocess.call(["ifconfig", interface, "down"])
    print(interface + " down.")
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    print("Changing MAC")
    subprocess.call(["ifconfig", interface, "up"])
    print(interface + " up.")


options = get_arguments()
change_mac(options.interface, options.new_mac)

# If you run from terminal, three of these commands will be executed without having to type in terminal.
