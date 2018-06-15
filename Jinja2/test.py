

t = Template(tmpl)
output_render = t.render(interface_list = interfaces, dev = device)

print output_render

timestr = time.strftime('%Y%m%d-%H%M%S')
output_file_name  = ('output-'+timestr+' '+CTT)
output_file = open (output_file_name , 'w')
output_file.write(output_render)
output_file.close()
