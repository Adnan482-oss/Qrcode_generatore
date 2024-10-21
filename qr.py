import qrcode
from PIL import Image

# Create a QRCode object with specified parameters
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Corrected the constant name
    box_size=10,
    border=1
)

# Add data to the QR code
qr.add_data("https://www.google.com")  # It's good practice to use "https://" for URLs

# Make the QR code
qr.make(fit=True)

# Customize the QR code's appearance and save it as an image
image = qr.make_image(fill_color="black", back_color="white")
image.save("name.png")
