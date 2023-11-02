# using the Asymmetric key algorithm: RSA
# to encrypt and decrypt a message | secret

# import necessary libraries: rsa & default_backend
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537, key_size=4096, backend=default_backend)

# check private_key
print(private_key)

# generate public key
public_key = private_key.public_key
public_key = private_key.public_key()

# check public_key
print(public_key)


# using the public_key to encrypt
# with padding and hashes

message = b"put something here"

encrypted = public_key.encrypt(message, padding.OAEP(mgf=padding.MGF1(
    algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

# check encrypted
print(encrypted)

# decrypting the secret

decrypted = private_key.decrypt(encrypted, padding.OAEP(mgf=padding.MGF1(
    algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

# check decrypted
print(decrypted)
