import os
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

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

# ruleid: cryptography-dsa
private_key = dsa.generate_private_key(
    key_size=1024,
)

params = dsa.generate_parameters(2048)

# ruleid: cryptography-dsa
private_key = params.generate_private_key()

# ok: cryptography-dsa
private_key = Ed25519PrivateKey.generate()
