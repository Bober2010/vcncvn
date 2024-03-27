from PIL import Image
x = int(input("   1 или 2   "))
if x == 1:
    image = Image.open('пп.jpg')
    new_image = image.crop((1230, 200, 1380, 350))
    new_image.save("icon_пп.jpg")
    new_image.show()
    image.close()
    new_image.close()
if x == 2:
    image = Image.open('аа.jpg')
    new_image = image.crop((200, 120, 370, 270))
    new_image.save("icon_аа.jpg")
    new_image.show()
    image.close()
    new_image.close()
