import qrcode

data = input("Enter text or URL: ")

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="pink", back_color="black")

filename = input("Enter file name (without .png): ")
img.save(f"{filename}.png")
print(f"QR Code saved as {filename}.png")
