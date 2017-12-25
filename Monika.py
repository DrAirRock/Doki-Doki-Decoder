import numpy as np 
import os
from PIL import Image 
import unicodedata
import binascii
import base64

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
    for y in range(0,height):
        for x in range(0,width):
            pixle = image.getpixel((x,y)) 
            if is_black(pixle): 
                b_array.append(0)
            elif is_white(pixle): 
                b_array.append(1)
    b_array = "".join(str(x) for x in b_array)
    return b_array

def bits2string(b): 
    print(b)
    return "".join([chr(int(x, 2)) for x in b])


def to_ascii(binary): 
    my_bytes = chunk(binary,8)
    array_of_bytes = []
    for byte in my_bytes: 
        array_of_bytes.append("".join(str(x) for x in byte))
    b = bits2string(array_of_bytes)
    return b

def read_monika(): 
    image = os.path.join('Char_files', 'monika_bytes.png') 
    monika_image = Image.open(image)
    return monika_image

def Convert_from_base64(encoded): 
    #encode to utf-8
    encoded = encoded.encode()
    #convert from base 64
    text = base64.decodestring(encoded)
    text = text.decode('utf-8')
    return text

def print_out(text): 
    with open(os.path.join('Decoded_Files', 'monika_decoded.txt'),'w') as out_file:
        out_file.write(text)
    out_file.close()

def main (): 
    image = read_monika()
    b = convert_to_binary(image)
    print(b)
    char_string = to_ascii(b)
    monika_string = Convert_from_base64(char_string)
    print_out(monika_string)



main()