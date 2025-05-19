import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

output_filename="message_10.enc"

password = b"10"
print(password)

salt = b"01"

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=1_200_000,
)
key = base64.urlsafe_b64encode(kdf.derive(password))
f = Fernet(key)

token = f.encrypt(b"mensaje secreto")

print(token)

with open(output_filename, 'wb') as file:
    token = file.write(token)

