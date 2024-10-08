import os

secret = "^IUhegeh957AEgf$^Aujeghnwe0283t2hyg0wdfhbsudb2409UHY4T9479(&y$t0H0h8"

# Vulnerable
user_input = input('What do you want to grep for?\n')
os.system("grep -R {} .".format(user_input))

# Vulnerable
user_input = input('Which directory do you want to list files in?\n')
os.popen("ls -l " + user_input)

# prints home directory
subprocess.call('echo $HOME', shell=True)

# throws an error
subprocess.call('echo {} $HOME'.format(secret), shell=False)
