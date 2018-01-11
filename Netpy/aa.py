from netmiko import ConnectHandler
import re
from sys import argv
from openpyxl import load_workbook

#script, command = argv

#mode = net_connect.find_prompt()

Col_A = []
Col_B = []
device_A = []
device_B = []
interface_A = []
interface_B = []

passed = {}
failed = {}

command = ("show cdp neigh")

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

def get_data(wb):
    sheet = wb.active
    first_column = sheet['A']
    for x in range(len(first_column)):
        Col_A.append(first_column[x].value)

    second_column = sheet['B']
    for y in range(len(second_column)):
        Col_B.append(second_column[y].value)
    return Col_A, Col_B


def get_parse(Col_A, Col_B):
    for word_A in Col_A:
        dev_A, int_A = word_A.split('_')
        device_A.append(dev_A)
        interface_A.append(int_A)

    for word_B in Col_B:
        dev_B, int_B = word_B.split('_')
        device_B.append(dev_B)
        interface_B.append(int_B)

    return device_A, interface_A, device_B, interface_B



def operation(device_A, interface_A, device_B, interface_B, output):
    for line in output:
        for dev_A, int_A, dev_B, int_B in zip(device_A, interface_A, device_B, interface_B):
            regex = ('%s''\s+''%s''\s+\d{3}\s+?.+\d+\s+''%s')% (dev_B, int_A, int_B)
            if dev_B in line:
                if re.search(regex, line):
                    passed[dev_B:int_B]
            else:
                failed[dev_B:int_B]
    return passed, failed




# Load external excel workbook
wb = load_workbook('bob.xlsx')

# function returns the column a and b of the excel sheet
Col_A, Col_B = get_data(wb)

# returns device and interfaces
device_A, interface_A, device_B, interface_B = get_parse(Col_A, Col_B)

# returns the output from the router
output = get_config(command)

# operation
passed, failed = operation(device_A, interface_A, device_B, interface_B, output)







#file_write(output)
#print (output)


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
