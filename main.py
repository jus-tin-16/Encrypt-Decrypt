# import required module
from cryptography.fernet import Fernet # type: ignore

# generate the key
key = Fernet.generate_key()

def writeToFile(file_path, content, mode="w"):
    try:
        with open(file_path, mode) as f:
            f.write(content)
        print(f"Message is saved in {file_path}")
    except IOError as e:
        print(f"Error: {e}")


def encryptFile(file_path, key):
    """Encryption function"""

    # write the key
    with open("filekey.key", "wb") as filekey:
        filekey.write(key)

    # opening the key
    with open("filekey.key", "rb") as filekey:
        key = filekey.read()

    # use the key
    fernet = Fernet(key)

    # open original file
    with open(file_path, "rb") as file:
        original = file.read()

    # encrypt the file
    encrypted = fernet.encrypt(original)

    # write encrypted file
    with open("encrypt.txt", "wb") as encrypted_file:
        encrypted_file.write(encrypted)


def decryptFile(file_path, key):
    """Decryption function"""
    # use the key
    fernet = Fernet(key)

    # opening the encrypted file
    with open(file_path, "rb") as enc_file:
        encrypted = enc_file.read()

    # decrypt the file
    decrypt = fernet.decrypt(encrypted)

    with open("decrypt.txt", "wb") as dec_file:
        dec_file.write(decrypt)

def readFile(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
        print(content)
    except FileNotFoundError:
        print("Error: The file 'example.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


print("Hello, user!")
print("This is a sample encrypt and decrypt activity")
message = input("Please enter a message: ")

writeToFile("message.txt", message)
encryptFile("message.txt", key)

opt = input("Would you like to view your message[y/n]:")

if opt == "y":
    decryptFile("encrypt.txt", key)
    readFile("decrypt.txt")

if opt == "n":
    readFile("encrypt.txt")