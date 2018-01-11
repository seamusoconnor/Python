import paramiko # module

ssh = paramiko.SSHClient() # Create ssh object

# "ssh" can be any variable

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Allow unknown host keys to be added to hostfile

ssh.connect("192.168.1.15", port = 22, username = "cisco", password = "cisco", allow_agent=False,look_for_keys=False) # conenct ot device last 2 vars are to prevent authentication errors



#stdin, stdout, stderr = ssh.exec_command("show run") # simple command that doesnt require input from user

stdin, stdout, stderr = ssh.exec_command("en") # command that requires further input

stdin.write("cisco") # The previous command requires the host and this will give it
stdin.write('\n')# This is a carraige return
stdin.flush() #
#stdin.write("source_test.txt") # source file
#stdin.write("\n")
#stdin.flush() #
#stdin.write("dest_file.txt")
#stdin.write("\n")






output = stdout.readlines() # This gives you the output stream

ssh.close() # close session
print '\n'.join(output) # and this splits it into a readble format - otherwise it's just a stream


#alternative to stdin to allow to deal with dynamic streams

#channel = ssh.invoke_shell() # starts invisible interactive shell session and get a dedicated socket channel push/pull commands

#channel.send() # send chars to shell
#channel.receive(9999) # channel recevie and the max number of chars we can rec
#channel.recv_ready() # check if there is dta to be read from the channel

#channel_data = str()
#host = str()
#srcfile = str()

#while True:i
#    if channel.recv_ready():
#        channel_data += channel.recv(9999)
#    else:
#        continue
#
#    if channel_data.endswith('D2#'): # if you have the following data incoming from the stream
#        channel.send("copy tftp: flash:\n") # send this string + the carraige return
#    elif channel_data.endswith('remote host []?'):
#        host = raw_input("\n\n\t Enter the TFTP Host IP: ")
#        channel.send(host)
#        channel.send('\n')
#    elif channel_data.endswith
