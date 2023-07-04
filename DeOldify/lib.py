from dep import rename_video, rename_image, limpar_pasta


from deoldify import device
from deoldify.device_id import DeviceId
from deoldify.visualize import *
import matplotlib.pyplot as plt
import torch
import warnings

def colorize_image(source, render_factor=25):
    rename_image(f'test_images/{source}')
    #NOTE:  This must be the first call in order to work properly!
    device.set(device=DeviceId.GPU0)
    
    plt.style.use('dark_background')
    torch.backends.cudnn.benchmark=True
    warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")
    
    colorizer = get_image_colorizer(artistic=True)

    source_path = 'test_images/image.png'
    result_path = colorizer.plot_transformed_image(path=source_path, render_factor=render_factor, compare=True)
    
    return result_path


def colorize_imageurl(source_url, source_path = 'test_images/image.png', render_factor=25):
    #NOTE:  This must be the first call in order to work properly!
    device.set(device=DeviceId.GPU0)
    
    plt.style.use('dark_background')
    torch.backends.cudnn.benchmark=True
    warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")
    
    colorizer = get_image_colorizer(artistic=True)


    result_path = colorizer.plot_transformed_image_from_url(url=source_url, path=source_path, render_factor=render_factor, compare=True) 
   
    return result_path


def colorize_video(file_name, render_factor=15):
    rename_video(f'video/source/{file_name}')    
    #NOTE:  This must be the first call in order to work properly!
    device.set(device=DeviceId.GPU0)
    
    plt.style.use('dark_background')
    warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")
    
    colorizer = get_video_colorizer()
    
    file_name_ext = 'video.mp4'
    result_path = colorizer.colorize_from_file_name(file_name_ext, render_factor=render_factor)
    
    limpar_pasta('video/bwframes')
    limpar_pasta('video/colorframes')

    return result_path


def colorize_videourl(source_url, render_factor=15):   
    #NOTE:  This must be the first call in order to work properly!
    device.set(device=DeviceId.GPU0)
    
    plt.style.use('dark_background')
    warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")
    
    colorizer = get_video_colorizer()
    
    file_name_ext = 'video.mp4'
    result_path = colorizer.colorize_from_url(source_url, file_name_ext, render_factor=render_factor)
    
    limpar_pasta('video/bwframes')
    limpar_pasta('video/colorframes')

    return result_path