from netmiko import ConnectHandler
from getpass import getpass

host = input("Enter your hostname: ")
command = input("Enter a valid IOS show command: ")
save_output_file = input("Enter the name of the file to save the output of the show command: ")

device1 = {
    "host": host,
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
    "session_log": save_output_file,
}

net_connect = ConnectHandler(**device1)
output = net_connect.send_command(command)
print(output)
print(net_connect.find_prompt())
