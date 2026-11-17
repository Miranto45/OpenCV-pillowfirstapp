from PIL import Image

im = Image.open("chat.jpg")

print(im.format, im.size, im.mode)

im.show()
