from netmiko import Netmiko
from getpass import getpass

password = getpass()
command = input("Enter a valid show command: ")

cisco3 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": 'cisco_ios',
    #"session_log": save_output_file,
}

cisco4 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": 'cisco_ios',
    #"session_log": save_output_file,
}

nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": 'cisco_nxos',
    #"session_log": save_output_file,
}

srx2 = {
    "host": "srx2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": 'juniper_junos',
    #"session_log": save_output_file,
}

for device in (cisco3, cisco4, nxos1, srx2):
    net_connect = Netmiko(**device)
    print(net_connect.find_prompt())
    output = net_connect.send_command(command)
    print(output)
    print(net_connect.find_prompt())
    
