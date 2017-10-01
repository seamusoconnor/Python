import os, time, yaml #Imports various libraries to work with
from netmiko import ConnectHandler #from netmiko library, import SSH ConnectHandler

os.system('clear') # Clears the screen

device = raw_input("Enter the device name: ") # Asks user for raw input

with open('net.yaml', 'r') as f: #opens a YAML file as read-only and as f
    doc = yaml.load(f) # loads Yaml file and assins it to variable doc

var1 = doc[device] ["dev"] # next lines read data from YAML using raw_input ot find correct tree
var2 = doc[device] ["ip"]
var3 = doc[device] ["user"]
var4 = doc[device] ["pass"]

print (device, var1, var2, var3, var4) # prints all variables associated with the device specified in the raw_input earlier


if device in open('net.yaml').read():
    net_connect = ConnectHandler(device_type = var1, ip = var2, username = var3, password = var4)    

#if device == "d2":
#    net_connect = ConnectHandler(device_type = var1, ip = var2, username = var3, password = var4)

#elif device == "seamus":
#    print " You entered Seamus"
#    exit()
else:
    print "Dunno, cannot find that data in the file"
    exit()




output = net_connect.send_command ("show run") # send raw_input as command to device
print output # prints the results of the raw input you entered to the remote device

file = open.("configuration.txt", "w")
file.write(output)
file.close()


exit()
