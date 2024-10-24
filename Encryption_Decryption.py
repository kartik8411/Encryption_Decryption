from cryptography.fernet import Fernet

#It is an example of symmetric encryption, where the same key is used for both encryption and decryption.

message = "hello how are u doing"

key = Fernet.generate_key()
fernet = Fernet(key)
encMessage = fernet.encrypt(message.encode())

print("original message: ", message)
print("encrypted message: ", encMessage)

decMessage = fernet.decrypt(encMessage).decode()
print("decrypted message: ", decMessage)