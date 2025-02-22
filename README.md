# AICTE_Project
This project hides a secret message inside an image using the Least Significant Bit (LSB) technique.
**How It Works:**
1] Load the image in VS Code.
2]Convert the secret message to binary.
3]Modify the least significant bits of the image pixels to store the message.
4]Save the encoded image.
5]To decode, extract and convert the hidden binary data back to text.

**Usage**
**Encoding**
Choose: 
1. Encode Message
2. Decode Message
Enter option (1/2): 1
Enter image file path: mypic.jpg
Enter secret message: File is hidden!!
Message hidden successfully in encoded_image.jpg

**Decoding**
Choose: 
1. Encode Message
2. Decode Message
Enter option (1/2): 2
Enter encoded image path: encoded_image.jpg
Decoded message: File is hidden!!


**Requirements**
-->Python 3.x
-->OpenCV (cv2)
-->NumPy (numpy)


