from cryptography.fernet import Fernet
import pyfiglet 
from colorama import Fore 

banner = pyfiglet.figlet_format('Symmetric Encrypt',font='doom')
print(Fore.GREEN + banner)

#It is an example of symmetric encryption, where the same key is used for both encryption and decryption.

message = "hello how are u doing"

key = Fernet.generate_key()
fernet = Fernet(key)
encMessage = fernet.encrypt(message.encode())

print("original message: ", message)
print("encrypted message: ", encMessage)

decMessage = fernet.decrypt(encMessage).decode()
print("decrypted message: ", decMessage)
