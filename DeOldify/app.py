# app.py
from flask import Flask, render_template, request, send_from_directory
import os
from lib import colorize_image, colorize_video
from dep import rename_image, rename_video
import shutil

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'test_images'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/imagem', methods=['GET','POST'])
def imagem():
    return render_template('imagem.html')
    
@app.route('/imagemcolorida', methods=['GET','POST'])
def imagemcolorida():
    file = request.files['image']
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        existing_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'image.png')
        if os.path.exists(existing_image_path):
            os.remove(existing_image_path)
        rename_image(f'test_images/{filename}')
        colorize_image('image.png')
        if os.path.exists('DeOldify/static/images/image.png'):
            os.remove('DeOldify/static/images/image.png')
        shutil.move('result_images/image.png', 'DeOldify/static/images/')
    return render_template('imagemcolorida.html')


@app.route('/download')
def download():
    return send_from_directory('static/images', 'image.png', as_attachment=True)



app.config['UPLOAD_VIDEO'] = 'video/source'


@app.route('/video', methods=['GET','POST'])
def video():
    return render_template('video.html')


@app.route('/videocolorido',  methods=['GET','POST'])
def videocolorido():
    file = request.files['video']
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_VIDEO'], filename))
        existing_image_path = os.path.join(app.config['UPLOAD_VIDEO'], 'video.mp4')
        if os.path.exists(existing_image_path):
            os.remove(existing_image_path)
        rename_video(f'video/source/{filename}')
        colorize_video('video.mp4')
        if os.path.exists('DeOldify/static/videos/video.mp4'):
            os.remove('DeOldify/static/videos/video.mp4')
        shutil.move('video/result/video.mp4', 'DeOldify/static/videos/')
    return render_template('videocolorido.html')



@app.route('/downloadvideo')
def download_video():
    return send_from_directory('static/videos', 'video.mp4', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
