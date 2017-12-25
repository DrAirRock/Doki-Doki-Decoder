import numpy as np 
import os
from PIL import Image 
import unicodedata
import binascii
import codecs
from base64 import b64decode
import struct

def chunk(array, n):
    for i in range(0, len(array), n):
        yield array[i:i+n]


def is_black(pixel): 
    if pixel == (0, 0, 0, 255):  
        return True
    else: 
        return False


def is_white(pixel): 
    if pixel == (255,255,255,255):
        return True
    else:
        return False

def convert_to_binary(image): 
    b_array = []
    width, height = image.size
    for x in range(0,width):
        for y in range(0,height):
            pixle = image.getpixel((x,y)) 
            print (pixle)
            if is_black(pixle): 
                b_array.append(0)
            elif is_white(pixle): 
                b_array.append(1)
    b_array = "".join(str(x) for x in b_array)
    return int(b_array)

def bits2string(b): 
    return "".join([b64encode(chr(int(x, 2))) for x in b])

def to_ascii(binary): 
    my_bytes = chunk(binary,8)
    array_of_bytes = []
    for byte in my_bytes: 
        array_of_bytes.append("".join(str(x) for x in byte))
    b = bits2string(array_of_bytes)
    #text = struct.pack("I", binary).endcode('base64')
    return text

def read_monika(): 
    image = os.path.join('Char_files', 'monika_bytes.png') 
    monika_image = Image.open(image)
    return monika_image


def main (): 
    image = read_monika()
    b = convert_to_binary(image)
    char_string = to_ascii(b)
    print (char_string)


main()