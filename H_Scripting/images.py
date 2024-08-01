from PIL import Image, ImageFilter

img = Image.open('.\\H_Scripting\\Pokedex\\pikachu.jpg')
# print(img.format)
# print(img.size)
# print(img.mode) # shows color format, HEX, RGB, etc
blurredImg = img.filter(ImageFilter.BLUR) # can also do SMOOTH SHARPEN ETC
greyImg = img.convert("L") # made image in back and white
crookedImg = img.rotate(90) # you can rotate the image
resizedImg = img.resize((200,200)) # you can make your image bigger or smaller
box = (100,100,400,400)
croppedImg = img.crop(box)

blurredImg.save("blur.png", "png")
greyImg.save("grey.png", "png")
crookedImg.save("crookedImg.png", "png")
resizedImg.save("resizedImg.png", "png")
croppedImg.save("croppedImg.png", "png")

greyImg.show() # opens up the file and shows you the image
print(img)

# size down a huge image
thumbnailImg = img.thumbnail((400,400))
thumbnailImg.save("thumbnailImg.png", "png")


