import os
import base64

def read_yuri():
    Yuri = open(os.path.join('Char_files', 'yuri.chr'),'r')
    Yuri_text = ""
    #read in the file
    for line in Yuri: 
        Yuri_text += line
    Yuri.close()
    return Yuri_text

def Convert_from_base64(encoded): 
    #encode to utf-8
    encoded = encoded.encode()
    #convert from base 64
    text = base64.decodestring(encoded)
    text = text.decode('utf-8')
    return text

def print_out(text): 
    with open(os.path.join('Decoded_Files', 'yuri_decoded.txt'),'w') as out_file:
        out_file.write(text)
    out_file.close()

def main(): 
    #dummy main
    Yuri_text = read_yuri()
    Decoded = Convert_from_base64(Yuri_text)
    print_out(Decoded)


main()