from cryptography.fernet import Fernet
def wite_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def encryptFile(filename,key):
    f= Fernet(key)
    with open(filename,"rb") as data:
        file_data = data.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename,"wb") as file:
        file.write(encrypted_data)

def decryptyFile(filename,key):
    f = Fernet(key)
    with open(filename,"rb") as file:
        encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
    with open(filename,"wb") as file:
        file.write(decrypted_data)
# wite_key()
key = load_key()
file = "E:\\python Scripts\\x.txt"
# encryptFile(file,key)
decryptyFile(file,key)

