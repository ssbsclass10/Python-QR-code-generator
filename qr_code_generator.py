#A Program in python to generate qrcode with the help of python.
import qrcode as qr
img= qr.make('secret.txt')
img.save('message.png')
print('Qr code successfully generated')