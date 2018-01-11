from matplotlib import pylab
from pylab import *
import wave
import os
import subprocess
import matplotlib.pyplot as plt
from skimage import color
from skimage import novice
from skimage import io



def graph():
    filename = os.path.join('Char_files', 'sayori.chr')
    command = ["ffmpeg", "-hide_banner", "-loglevel", "panic", "-i", filename, "-f", "wav", "-"]
    converter = subprocess.Popen(command, stdout=subprocess.PIPE)
    sig = wave.open(converter.stdout, 'r')
    xsig = sig.readframes(214748000)
    xsig = fromstring(xsig, 'Int16')
    f = sig.getframerate()
    spectrogram = specgram(xsig[0:214748000], Fs = f, scale_by_freq=True, sides='default')
    print(spectrogram)
    plt.axis([0, 6.25, 4000, 22000])
    set_aspect('equal')
    title('DOKI DOKI QR');
    #show()
    plt.savefig(os.path.join('Decoded_Files', 'sayoir_dirty.jpeg'))
    sig.close()


def value_limit(pixel): 
    if pixel[2] < .80:  
        return True
    else: 
        return False


def convert_filter(hsv_image, rgb_image): 
    b_array = []
    print("hello")
    ndims = hsv_image.shape
    height  = ndims[0] - 1
    width = ndims[1] - 1
    print(height)
    print(width)
    for x in range(0,height):
        for y in range(0,width):
            pixel = hsv_image[x,y]
            if value_limit(pixel): 
                rgb_image[x,y] = [1,1,1]
            else: 
                rgb_image[x,y] = [0,0,0]
        
    return rgb_image


def read_file():
    fname = os.path.join('Decoded_Files', 'sayoir_dirty.jpeg')
    print(fname) 
    dirty = io.imread(fname)
    print(dirty)
    hsv_dirty = color.rgb2hsv(dirty)
    return hsv_dirty


def main(): 
    graph()
    image = read_file()
    image2 = color.hsv2rgb(image)
    print(image2)
    b_array = convert_filter(image,image2)
    print(b_array)
    io.imsave("test.png",b_array)


main()