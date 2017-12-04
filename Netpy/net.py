from netmiko import ConnectHandler
import re

#mode = net_connect.find_prompt()

def get_config():
    net_connect = ConnectHandler(device_type='cisco_ios', ip='192.168.1.12', username='cisco', password='cisco', secret='cisco')
    net_connect.enable()
    mode = net_connect.find_prompt()
    print (mode)
    output = net_connect.send_command('sh run').splitlines()
    net_connect.disconnect()
    return output


output = get_config()

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
