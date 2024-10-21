import qrcode
from PIL import Image

qr=qrcode.QrCode(version=1,error_correction=qrcode.constant.CORRECT_ERROR_H,
box_size=10,border=1)

qr.add_data("")
qr.make(True)

image=qr.make_image(fill_color="black",back_color="white")
image.save("")
