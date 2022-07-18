import qrcode
from pathlib import pathlib

arquivo = path("codigoQr.png")
data = "Daniel e Thamires"
img = qrcode.make('Daniel ama a Thamires')
type(img)  # qrcode.image.pil.PilImage
img.save(arquivo)
