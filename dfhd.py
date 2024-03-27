from PIL import Image
x = int(input("   1 или 2   "))
if x == 1:
    image = Image.open('пп.jpg')
    new_image = image.crop((0, 0, image.width/2, 1200))
    new_image.save("cropped_img.jpg")
    new_image.show()
    image.close()
    new_image.close()
if x == 2:
    image = Image.open('пп.jpg')
    new_image = image.crop((image.width/2, 0, 1920, 1200))
    new_image.save("cropped_img.jpg")
    new_image.show()
    image.close()
    new_image.close()
