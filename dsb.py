from PIL import Image
x = input("   обрезать???   ")
if x == "обрезать":
    q = int(input("цифру пиши"))
    image = Image.open('пп.jpg')
    new_image = image.crop((0, 0, q, q))
    new_image.save("пп.jpg")
    new_image.show()
    image.close()
    new_image.close()
else:
    print("нет такой команды")