import paramiko # module

ssh = paramiko.SSHClient() # Create ssh object

# "ssh" can be any variable

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Allow unknown host keys to be added to hostfile

ssh.connect("192.168.1.232", port = 22, username = "cisco", password = "cisco", allow_agent=False,look_for_keys=False) # conenct ot device last 2 vars are to prevent authentication errors

#stdin, stdout, stderr = ssh.exec_command("show run") # simple command that doesnt require input from user

stdin, stdout, stderr = ssh.exec_command("copy tftp: flash") # command that requires further input

stdin.write("1.1.1.1") # The previous command requires the host and this will give it
stdin.write('\n')# This is a carraige return
stdin.flush() #
stdin.write("source_test.txt") # source file
stdin.write("\n")
stdin.flush() #
stdin.write("dest_file.txt")
stdin.write("\n")



output = stdout.readlines() # This gives you the output stream

ssh.close() # close session
print '\n'.join(output) # and this splits it into a readble format - otherwise it's just a stream