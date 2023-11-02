# Using the Fernet implementation
# of the AES algorithm

from cryptography.fernet import Fernet

# generate key
key = Fernet.generate_key()
f = Fernet(key)
message_or_secret = b"Secrets go here"

# encrypt the message_or_secret
encrypted = f.encrypt(message_or_secret)
print(encrypted)

# to decrypt the data using a Fernet object
f_d = Fernet(key)
decrypted = f_d.decrypt(encrypted)
print(decrypted)
