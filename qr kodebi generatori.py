import image
import qrcode
qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)
data="https://www.facebook.com/nika.nikoloz.102"

qr.add_data(data)
qr.make(fit = True)
image= qr.make_image(fill="black", back_color= "white" )
image.save("qr kodi")