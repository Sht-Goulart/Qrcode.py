from email.mime import image
import qrcode

image_qr = qrcode.make("") #passar o link para criar o qrcode
image_qr.save("qrcode.python.jpg")