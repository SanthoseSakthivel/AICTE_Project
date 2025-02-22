import cv2
import numpy as np

def encode_message(image_path, secret_message, output_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return

    secret_message += "####"  # Delimiter to mark the end of the message
    message_bin = ''.join(format(ord(char), '08b') for char in secret_message)
    index = 0

    for row in img:
        for pixel in row:
            for color in range(3):  # Modify RGB values
                if index < len(message_bin):
                    pixel[color] = (pixel[color] & 0xFE) | int(message_bin[index])
                    index += 1

    cv2.imwrite(output_path, img)
    print(f"Message hidden successfully in {output_path}")

def decode_message(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return

    message_bin = ""
    for row in img:
        for pixel in row:
            for color in range(3):
                message_bin += str(pixel[color] & 1)

    message = ''.join(chr(int(message_bin[i:i+8], 2)) for i in range(0, len(message_bin), 8))
    extracted_message = message.split("####")[0]  # Stop at the delimiter

    print(f"Decoded message: {extracted_message}")

# User Input
option = input("Choose: \n1. Encode Message\n2. Decode Message\nEnter option (1/2): ")

if option == "1":
    img_path = input("Enter image file path: ")
    message = input("Enter secret message: ")
    output_path = "encoded_image.jpg"
    encode_message(img_path, message, output_path)
elif option == "2":
    img_path = input("Enter encoded image path: ")
    decode_message(img_path)
else:
    print("Invalid option selected!")

