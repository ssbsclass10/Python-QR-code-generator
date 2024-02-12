import qrcode
from PIL import Image

#Creating varable to design QR code
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=18, border=4,)
qr.add_data("https://www.youtube.com/@gwashis7028")
qr.make(fit=True)
img=qr.make_Image(fill_color='blue',back_color='yellow')
img.save('GW-ASHIS_YT.png')

