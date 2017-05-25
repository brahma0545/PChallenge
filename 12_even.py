from PIL import Image
image = Image.open("Data/cave.jpg")
print (image.size)
nsize = tuple([x/2 for x in image.size])
odd = even = Image.new(image.mode, nsize)

for x in range(image.size[0]):
    for y in range(image.size[1]):
        if x % 2 == 0 and y % 2 == 0:
            even.putpixel((x/2, y/2), image.getpixel((x, y)))
        if x % 2 == 1 and y % 2 == 1:
            odd.putpixel((x / 2, y / 2), image.getpixel((x, y)))
        if x % 2 == 1 and y % 2 == 0:
            even.putpixel((x/2, y/2), image.getpixel((x, y)))
        if x % 2 == 0 and y % 2 == 1:
            odd.putpixel((x/2, y/2), image.getpixel((x, y)))

even.save("Data/even.jpg")
odd.save("Data/odd.jpg")
