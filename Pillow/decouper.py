from PIL import Image

with Image.open("chat.jpg") as im:
    zone = (100, 100, 300, 300)
    region = im.crop(zone)
    region = region.transpose(Image.Transpose.ROTATE_180)
    im.paste(region, zone)
    im.save("chat_modifie.jpg")
    im.show()
