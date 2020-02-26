# Import Regular Expression and IPy modules
import re
from IPy import IP

routing_table_file = open('<FILE PATH HERE>')

# This function will take in a list of IP's and return a sorted list
def sort_ip_list(ip_list):
    """Sort an IP address list."""
    ipl = [(IP(ip).int(), ip) for ip in ip_list]
    ipl.sort()
    return [ip[1] for ip in ipl]

routing_table = routing_table_file.read()

# This regular expression match object will match all /22 (or /29 or whatever needed) subnets from a routing table
# with the syntax: S       172.28.116.0/22 [10/0] via 192.168.250.2, Internal
ip_address_mask22_regex = re.compile(r'\w\s+(\d+.\d+.\d+.\d+/22)\s\[\d+/\d+\]\s\w+\s192.168.250.2,\s\w+')
ip_address_mask29_regex = re.compile(r'\w\s+(\d+.\d+.\d+.\d+/29)\s\[\d+/\d+\]\s\w+\s192.168.250.2,\s\w+')

# Find all the matches and save them to a list
first_list_ip_addresses_to_250_2 = ip_address_mask22_regex.findall(routing_table)
second_list_ip_addresses_to_250_2 = ip_address_mask29_regex.findall(routing_table)

# Sort the list of IP addresses and print it
ip_list_sorted = sort_ip_list(first_list_ip_addresses_to_250_2)
for ip in ip_list_sorted:
    print(ip + '\n')


ip_list_sorted = sort_ip_list(second_list_ip_addresses_to_250_2)
for ip in ip_list_sorted:
    print(ip + '\n')
