import pyqrcode
import png
from pyqrcode import QRCode

generate_qr = input("Digite o link para gerar o QRCode: ")

url = pyqrcode.create(generate_qr)

url.svg("myqr.svg", scale = 8)

url.png("myqr.png", scale = 6)