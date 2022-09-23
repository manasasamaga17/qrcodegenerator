
import qrcode  qr=qrcode.QRCode(     version=15,#version of the qrcode, higher the number bigger the qr code image and complicated picture     
box_size=10,#size of the box in which qr code will be displayed     
border=5 #it is the white part of image, border in all 4 sides with white color ) 
qr.add_data("data") 
qr.make(fit=True) 
img=qr.make_image(fill="black", back_color="white") 
img.save("test.png")
