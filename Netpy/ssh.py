
import os
import time

from netmiko import ConnectHandler

os.system("clear")
time.sleep(1)

host = raw_input ("Enter Host IP: ")
username = raw_input ("Enter username: ")
password = raw_input ("Enter password: ")
command_input = raw_input ("Enter Command: ")


platform = 'cisco_ios'

device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)

output = device.send_command(command_input)

print output
