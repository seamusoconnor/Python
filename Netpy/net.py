from netmiko import ConnectHandler
import re
from sys import argv

script, command = argv

#mode = net_connect.find_prompt()

def get_config(command):
    net_connect = ConnectHandler(device_type='cisco_ios', ip='192.168.1.15', username='cisco', password='cisco', secret='cisco')
    mode = net_connect.find_prompt()
    print (mode)
    net_connect.enable()
    mode = net_connect.find_prompt()
    print (mode)
    output = net_connect.send_command(command).splitlines()
    net_connect.disconnect()
    return output

def file_write(output):
    print('inside loop')
    file = open('netfile.txt','w')
    file.write(output)
    file.close()

output = get_config(command)
#file_write(output)

print (output)
































#net_connect.config_mode() -- Enter into config mode
#net_connect.check_config_mode() -- Check if you are in config mode, return a boolean
#net_connect.exit_config_mode() -- Exit config mode
#net_connect.clear_buffer() -- Clear the output buffer on the remote device
#net_connect.enable() -- Enter enable mode
#net_connect.exit_enable_mode() -- Exit enable mode
#net_connect.find_prompt() -- Return the current router prompt
#net_connect.commit(arguments) -- Execute a commit action on Juniper and IOS-XR
#net_connect.disconnect() -- Close the SSH connection
#net_connect.send_command(arguments) -- Send command down the SSH channel, return output back#
#net_connect.send_config_set(arguments) -- Send a set of configuration commands to remote device
#net_connect.send_config_from_file(arguments) -- Send a set of configuration commands loaded from a file
