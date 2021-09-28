from netmiko import ConnectHandler
import datetime

# Firewall host that we want to SSH into:
my_fw = {'host': '<hostname>',
         'device_type': 'fortinet',
         'ip': '192.168.100.1', # Firewall IP accessed by this machine
         'username': '<backup user>', # as created on the firewall
         'password': '<secure password>'}

net_connect = ConnectHandler(**my_fw) # Create connect handler object

output = net_connect.send_command('show full-configuration') # SSH and send command to the firewall and save the output

current_time = datetime.datetime.today().strftime('%Y_%b_%d') # This is to add to the naming of the file

# Create a file and write the output on it. Make sure the directory is valid on this machine:
with open('/home/fortigate_backups/' + str(my_fw['host']) + '_' + str(current_time) + '.conf', 'w') as f:
    for line in output:
        f.write(line)
