from PIL import Image
x = int(input("   1 или 2 или 3   "))
if x == 1:
    image = Image.open('пп.jpg')
    new_image = image.crop((0, 0, 1200, 1200))
    new_image.save("cropped_img.jpg")
    new_image.show()
    image.close()
    new_image.close()
if x == 2:
    image = Image.open('аа.jpg')
    new_image = image.crop((0, 0, 1200, 1200))
    new_image.save("cropped_img.jpg")
    new_image.show()
    image.close()
    new_image.close()
if x == 3:
    image = Image.open('ва.jpg')
    new_image = image.crop((0, 0, 1200, 1200))
    new_image.save("cropped_img.jpg")
    new_image.show()
    image.close()
    new_image.close()

