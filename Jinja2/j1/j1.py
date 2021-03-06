from jinja2 import Template
import yaml
from sys import argv
import time

script, CTT = argv


file = open ('tmpl.j1','r')
tmpl = file.read()

var_file = open("var.j1","r")
var = yaml.load(var_file.read())

device = var['device_name']
var_interfaces = var['interfaces']
interfaces = var_interfaces.split(",")


t = Template(tmpl)
output_render = t.render(interface_list = interfaces, dev = device)

print output_render

timestr = time.strftime('%Y%m%d-%H%M%S')
output_file_name  = ('output-'+timestr+' '+CTT)
output_file = open (output_file_name , 'w')
output_file.write(output_render)
output_file.close()
