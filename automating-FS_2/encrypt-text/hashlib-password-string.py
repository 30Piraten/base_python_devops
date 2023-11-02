# import hashlib lib
import hashlib

# define secret password or  doc
secret = "This is a passwrd or doc text."

# encode secret if string or doc
bsecret = secret.encode()

# determine hashlib algorithm
m = hashlib.md5()

# update binary secret
m.update(bsecret)

# call digest
m.digest()
print(m.digest())
