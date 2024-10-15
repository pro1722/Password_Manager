Overview: 
This is a simple password manager that allows users to securely store their account names and passwords using encryption. 
The program enables users to add new passwords and view existing ones, all while ensuring that passwords are encrypted before 
storage and decrypted when accessed.


Features:
1.Secure Encryption: Passwords are encrypted using the cryptography.fernet module before being saved to a file.
2.Password Strength Check: The program checks the strength of a password based on length, case, digit, and special characters.
3.Add or View Passwords: Users can add new passwords or view existing ones in an encrypted manner.


Requirements:
Python 3.x

Cryptography package:
You can install the cryptography module using:
pip install cryptography


How to Use:
Generate Encryption Key: First, you need to generate a key and store it in a file named key.key. You can generate a key using the following code snippet:
from cryptography.fernet import Fernet
key = Fernet.generate_key()
with open("key.key", "wb") as key_file:
    key_file.write(key)

This key will be used to encrypt and decrypt passwords.

Run the Program: 
The password manager program provides two modes:

1.View Passwords: Decrypt and display the stored passwords.
2.Add New Password: Encrypt and store new passwords.
To run the program, simply execute the Python script:
python password_manager.py

Commands:
1.To view existing passwords, choose view when prompted.
2.To add a new password, choose add and provide the account name and password.

Password Strength: 
When adding a new password, the program will check its strength based on the following criteria:

1.Length of at least 8 characters
2.Contains uppercase letters
3.Contains lowercase letters
4.Contains digits
5.Contains special characters
6.Password strength will be rated as "Weak" or "Strong."

Exit: To quit the program, press q when prompted.

File Structure:
password_manager.py: The main script containing the password management logic.
key.key: A file that stores the encryption key.
passwords.txt: The file where account names and encrypted passwords are stored.
Security Considerations
Keep the key.key file safe, as it is required to decrypt your passwords. If you lose it, you will not be able to recover your encrypted passwords.
Avoid sharing your passwords.txt or key.key file with others to ensure your passwords remain secure.
