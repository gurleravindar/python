from cryptography.fernet import Fernet
import re

referenceId = input('Please enter REFERENCE ID \n')

key = Fernet.generate_key()
cipher_suite = Fernet(key)
encoded_text = '' 

if(len(referenceId)==12):
    # allowing some specail characters
    if(bool(re.search('[a-zA-Z0-9!@#$%]', referenceId))):
        encode_string =  referenceId.encode()
        encoded_text = cipher_suite.encrypt(encode_string)
        print("Encrypted text", encoded_text)

        user_option = input('Are you sure want to decrypt: (y/n)')
        if(user_option == 'y' or user_option == 'Y'):
            decrypted_text = cipher_suite.decrypt(encoded_text)
            print("Decrypted text", decrypted_text)
else:
    print('Please enter 12 digit reference id')
    exit







