import os

# Vulnerable
user_input = input('What do you want to grep for?\n')
os.system("grep -R {} .".format(user_input))

# Vulnerable
user_input = input('Which directory do you want to list files in?\n')
os.popen("ls -l " + user_input)

# prints home directory
subprocess.call('echo $HOME', shell=True)

# throws an error
subprocess.call('echo $HOME', shell=False)
