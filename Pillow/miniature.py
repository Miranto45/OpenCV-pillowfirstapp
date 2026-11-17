import os
from PIL import Image

fichiers = ["image1.png", "image2.bmp"]

for infile in fichiers:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
            
                im.convert("RGB").save(outfile)
                print(f"Converti : {outfile}")
        except OSError:
            print("Impossible de convertir :", infile)
