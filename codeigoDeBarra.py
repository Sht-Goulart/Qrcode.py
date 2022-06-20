from barcode import EAN13
from barcode.write import ImageWrite

codigo_prod = {
    "feijão": "123456789123",
    "Arroz": "123456789124",
    "Bolacha": "123456789125",
    "Ovo": "123456789126"
}

for prod in codigo_prod:
    codigo = codigo_prod[prod]
    codigo_barra = EAN13(codigo, write = ImageWrite())
    codigo_barra.save(f"codigo_barra_{prod}")