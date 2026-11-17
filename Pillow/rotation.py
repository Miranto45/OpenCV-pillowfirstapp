from PIL import Image

with Image.open("chat.jpg") as im:
    im_redim = im.resize((256, 256))
    im_tournee = im_redim.rotate(45)
    im_tournee.save("chat_rotation.jpg")
    im_tournee.show()
