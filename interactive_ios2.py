from netmiko import ConnectHandler
from getpass import getpass

host1 = input("Enter hostname dev1: ")
host2 = input("Enter hostname dev2: ")

username = input("Enter the username: ")
password = input("Enter the password: ")
command = input("Enter a valid IOS show command: ")
save_output_file = input("Enter the name of the file to save the output of the show command: ")

device1 = {
    "host": host1,
    "username": username,
    "password": password,
    "device_type": 'cisco_ios',
    "session_log": save_output_file,
}

device2 = {
    "host": host2,
    "username": username,
    "password": password,
    "device_type": 'cisco_ios',
    "session_log": save_output_file,
}



net_connect1 = ConnectHandler(**device1)
output1 = net_connect1.send_command(command)
print(net_connect1.find_prompt())
print(output1)
print(net_connect1.find_prompt())

net_connect2 = ConnectHandler(**device2)
output2 = net_connect2.send_command(command)
print(net_connect2.find_prompt())
print(output2)
print(net_connect2.find_prompt())
