from PIL import Image, ImageFilter, ImageEnhance

with Image.open("chat.jpg") as im:
    im_floue = im.filter(ImageFilter.BLUR)
    im_floue.save("chat_flou.jpg")

    ameliorateur = ImageEnhance.Contrast(im)
    im_contraste = ameliorateur.enhance(1.5)
    im_contraste.save("chat_contraste.jpg")
    im_contraste.show()
