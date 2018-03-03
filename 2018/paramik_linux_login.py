import paramiko

ssh = paramiko.SSHClient() # Create ssh object
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Allow unknown host keys to be added to hostfile



ssh.connect("192.168.1.23", port = 22, username = "USERNAME", password = "PASSWORD", allow_agent=False,look_for_keys=False) # Connect to device. Last 2 variables are to prevent authentication errors

stdin, stdout, stderr = ssh.exec_command("uname -a") # input, output, errors. This command is for non-interactive commands

output = stdout.readlines() # Take output from the command ran and assign it as output

print output

