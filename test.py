from steganography.steganography import Steganography
from datetime import datetime
import imghdr
#imghdr.what('/tmp/bass')

import imageio





def send_message():

    original_image = "input.jpg"

    #imghdr.what('E:\spychat')
    output_path = "output.jpg"
    text = input("what do you want to say")
    Steganography.encode(original_image, output_path, text)

    print("Encryption complete")

try:

    im=imageio.open("original_image")

    send_message()

except IOError:

    print Exception





def read_mesage():

    output_path = input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    print secret_text





try:

    im=Image.open("input.jpg")

    # do stuff

except IOError:

    print Exception

