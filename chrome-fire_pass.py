try:
    import firefox_decrypt
except TypeError:
    print('You need to use Python 3.9.')
    exit()
import decrypt_chrome_password

try:
    decrypt_chrome_password.main()
    print("'chrome_passwords.txt' ready")
except:
    print("Couldn't retrieve Chrome passwords.\nTrying with Firefox instead.")

try:
    firefox_decrypt.main()
    print("'firefox_passwords.txt' ready")
except:
    print("Couldn't retrieve Chrome passwords.")