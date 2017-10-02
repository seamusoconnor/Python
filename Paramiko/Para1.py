import paramiko

ssh = paramiko.SSHClient() # Create ssh object

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Allow unknown hosts

ssh.connect("192.168.1.232", port = 22, username = "cisco", password = "cisco", allow_agent=False,look_for_keys=False) # conenct ot device last 2 vars are to prevent authentication errors

stdin, stdout, stderr = ssh.exec_command("show ip int brief | ex unass") #

output = stdout.readlines()

print '\n'.join(output)


