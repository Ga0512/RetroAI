import os
import shutil
import smtplib
import email.message

def envio(sub, email_envio, corpo): 
    msg = email.message.Message()
    msg['Subject'] = str(sub)
    msg['From'] = ''
    msg['To'] = str(email_envio)
    password = 'shsxrmqbwndoskvp' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))



def mover_imagem(origem, destino, nome_imagem):
    # Construa o caminho completo para a imagem de origem
    caminho_origem = os.path.join(origem, nome_imagem)
    
    # Construa o caminho completo para o destino
    caminho_destino = os.path.join(destino, nome_imagem)
    
    try:
        # Move a imagem para o destino
        shutil.move(caminho_origem, caminho_destino)
        print(f"Imagem {nome_imagem} movida de {origem} para {destino}")
    except FileNotFoundError:
        print(f"A imagem {nome_imagem} não foi encontrada em {origem}")
    except PermissionError:
        print(f"Permissão negada para mover a imagem {nome_imagem}")




def rename_video(video_path, new_video_name='video.mp4'):
    video_dir, video_file = os.path.split(video_path)
    new_video_path = os.path.join(video_dir, new_video_name)
    os.rename(video_path, new_video_path)
    return new_video_path


def rename_image(image_path, new_image_name='image.png'):
    image_dir, image_file = os.path.split(image_path)
    new_image_path = os.path.join(image_dir, new_image_name)
    os.rename(image_path, new_image_path)
    return new_image_path


# limpar pasta
def limpar_pasta(caminho_pasta):
    # Verifica se o caminho fornecido é uma pasta
    if not os.path.isdir(caminho_pasta):
        print(f"{caminho_pasta} não é uma pasta válida.")
        return

    # Percorre todos os arquivos e subpastas na pasta
    for nome_arquivo in os.listdir(caminho_pasta):
        caminho_item = os.path.join(caminho_pasta, nome_arquivo)
        
        # Verifica se é um arquivo
        if os.path.isfile(caminho_item):
            os.remove(caminho_item)
            
        
        # Verifica se é uma subpasta
        elif os.path.isdir(caminho_item):
            shutil.rmtree(caminho_item)