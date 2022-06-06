import numpy as np
from PIL import Image


def image_mode(mode):
    if mode == 'RGB':
        return 3
    elif mode == 'RGBA':
        return 4

def encode_array(image_array, binary_message, req_pixels, total_pixels):
    index = 0
    for i in range(total_pixels):
        for j in range(0, 3):
            image_array[i][j] = encode_pixel(
                image_array[i][j], binary_message[index])
            index += 1
            if index > req_pixels-1:
                return image_array


def encode_pixel(value1, value2):
    value2 = int(value2)
    if value1 == 255:
        if value2 == 1:
            return value1
        else:
            return value1-1
    bin_value1 = int(str(bin(value1))[-1])
    if bin_value1 == value2:
        return value1
    else:
        return value1+1


def Encode(src, message, dest, key):

    img = Image.open(src, 'r')
    
    if img.format != "PNG":
        return 2        
    
    width, height = img.size
    image_array = np.array(list(img.getdata()))
    total_pixels = width*height
    message += key
    binary_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(binary_message)
    if req_pixels > total_pixels*3:
        return 1

    else:
        image_array = encode_array(
            image_array, binary_message, req_pixels, total_pixels)
        n = image_mode(img.mode)
        image_array = image_array.reshape(height, width, n)
        enc_img = Image.fromarray(image_array.astype('uint8'), img.mode)
        enc_img.save(dest)
        return 0


def extract_last_bit(array, total_pixels):
    hidden_bits = []

    for p in range(total_pixels):
        for q in range(3):
            value = bin(array[p][q])
            value = value[-1]
            hidden_bits += value
    return hidden_bits


def eight_bit_pattern(encoded_hidden_message):
    
    eight_bit_combined = []
    for i in range(0, len(encoded_hidden_message), 8):
        eight_bit_combined += ["".join(encoded_hidden_message[i:i+8])]
    return eight_bit_combined


def decoded_message(binary_hidden_message):
    decoded_message_text = []

    for i in binary_hidden_message:
        decoded_message_text += [chr(int(i, base=2))]

    decoded_message_text = "".join(decoded_message_text)
    return decoded_message_text


def Decode(src, key):

    img = Image.open(src, 'r')
    image_array = np.array(list(img.getdata()))

    total_pixels = img.size[0]*img.size[1]

    encoded_hidden_message = extract_last_bit(image_array, total_pixels)
    eight_bit_combined = eight_bit_pattern(encoded_hidden_message)
    binary_hidden_message = list(map(str, eight_bit_combined))
    decoded_message_text = decoded_message(binary_hidden_message)
    end = decoded_message_text.find(key)
    if end == -1:
        return 1
    else:
        return decoded_message_text[0:end]

def main2():

    key = "123"
    code = Encode("1.png", "Divyanshu"*11, "2.png", key)
    
    if code == 0:
        print("Image Encoded Successfully")
    elif code == 1:
        print("ERROR: Need larger file size")
    elif code == 2:
        print("ERROR: Not a png file")

    code = Decode("2.png", key)
    
    if code == 1:
        print("No Hidden Message Found")
    else:
        print("Hidden Message is : " + code)
    pass

main2()
