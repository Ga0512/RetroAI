# app.py
from flask import Flask, render_template, request, send_from_directory, redirect, make_response, send_file
import os
from lib import colorize_image, colorize_video
from dep import mover_imagem, envio
import shutil
import requests
import json


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'test_images'
confirm_login = ['']
confirm = ['']

url = 'https://retroai-803fe-default-rtdb.firebaseio.com'

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    global confirm

    if request.method == 'POST':
        email = request.form.get('user')
        senha = request.form.get('password')

        requisição = requests.get(f'{url}/usuarios/.json')

        api_response = requisição.json()

        found = False
        for key, value in api_response.items():
            if value['email'] == email:
                found = True
                break

        if found:
            confirm[0] = 'Email já usado'

        else:
            confirm[0] = ''
            data = {'email': email, 'senha': senha}
            requisição = requests.post(f'{url}/usuarios/.json', data=json.dumps(data))
            
            resp = make_response(redirect('/'))

            resp.set_cookie('email', str(email))
            resp.set_cookie('senha', str(senha))

            return resp
        

    confi = confirm[0]
    confirm.clear()
    confirm = ['']
    
    return render_template('cadastro.html', confirm=confi)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global confirm_login

    requisição = requests.get(f'https://retroai-803fe-default-rtdb.firebaseio.com/usuarios/.json')

    api_response = requisição.json()

    email_cooked = request.cookies.get("email")
    senha_cooked = request.cookies.get("senha")
    
    if email_cooked and senha_cooked != 'None':
        for key, value in api_response.items():
            if value['email'] == email_cooked and value['senha'] == senha_cooked:
               return redirect('/')

    if request.method == 'POST':
        user = request.form.get('user')
        senha = request.form.get('password')

        requisição = requests.get(f'{url}/usuarios/.json')

        api_response = requisição.json()

        found = False
        for key, value in api_response.items():
            if value['email'] == user and value['senha'] == senha:
                found = True
                break

        if found:
            confirm_login[0] = ''
            resp = make_response(redirect('/'))

            resp.set_cookie('email', str(user))
            resp.set_cookie('senha', str(senha))

            return resp

        else:
            confirm_login[0] = 'Usuário não encontrado...'


    confirma_login = confirm_login[0]
    confirm_login.clear()
    confirm_login = ['']
    
    return render_template('login.html', confirm=confirma_login)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/imagem', methods=['GET','POST'])
def imagem():
    requisição = requests.get(f'{url}/usuarios/.json')

    api_response = requisição.json()

    email_cooked = request.cookies.get("email")
    senha_cooked = request.cookies.get("senha")

    if email_cooked and senha_cooked != 'None':
        
        found = False
        for key, value in api_response.items():
            if value['email'] == email_cooked and value['senha'] == senha_cooked: 
                found = True
                break

        if found:
            if request.method == 'POST':
                file = request.files['image']
                filename = file.filename
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                colorize_image(str(filename))
                mover_imagem('result_images', 'DeOldify/static/images', str(filename))
                os.remove(f'test_images/{str(filename)}')
                
                return redirect(f'/static/images/{str(filename)}')
            
                
                
            return render_template('imagem.html')
            

        else:
            return redirect('/login')

    else:
        return redirect('/login')
    

app.config['UPLOAD_VIDEO'] = 'video/source'


@app.route('/video', methods=['GET','POST'])
def video():
    requisição = requests.get(f'{url}/usuarios/.json')

    api_response = requisição.json()

    email_cooked = request.cookies.get("email")
    senha_cooked = request.cookies.get("senha")

    if email_cooked and senha_cooked != 'None':
        
        found = False
        for key, value in api_response.items():
            if value['email'] == email_cooked and value['senha'] == senha_cooked: 
                found = True
                break

        if found:
            if request.method == 'POST':
                file = request.files['video']
                filename = file.filename
                file.save(os.path.join(app.config['UPLOAD_VIDEO'], filename))
                colorize_video(str(filename))
                mover_imagem('video/result', 'DeOldify/static/videos', str(filename))
                os.remove(f'video/source/{str(filename)}')

                corpo_email = f"""Boas notícias, seu vídeo foi colorido com sucesso! <br>
                                Acesse, compartilhe e faça download do seu vídeo: <br>
                                <br>
                                <a href="https://retroai.onrender.com/static/videos/{filename}"> Acesse seu vídeo colorido aqui!</a>"""
                               

                # enviar email aqui
                envio ("Seu vídeo está colorido! 🎨", str(email_cooked), corpo_email)

                return redirect(f'/static/videos/{str(filename)}')
                
            
            return render_template('video.html')

        else:
            return redirect('/login')

    else:
        return redirect('/login')
    

if __name__ == '__main__':
    app.run(debug=True)
