from PIL import Image, ImageFilter
import re
image = Image.open("Data/oxygen.png")
# img = image.convert('RGB')
print (image.size)
print (image.getpixel((0, 45)))

source = image.split()
R, G, B = 0, 1, 2
mask = source[R].point(lambda i: i < 100 and 255)
out = source[G].point(lambda i: i*0.7)
source[G].paste(out, None, mask)
im = Image.merge(image.mode, source)
# im.show()
# image.show()
row = [image.getpixel((x, 45)) for x in range(0, image.size[0], 7)]
ords =[r for r, g, b, a in row if r == b == g]
print (row)
print ords
print ("".join(map(chr, ords)))
print (re.findall("\d+", "".join(map(chr, ords))))
print (map(int, re.findall("\d+", "".join(map(chr, ords)))))
print ("".join(map(chr, map(int, re.findall("\d+", "".join(map(chr, ords)))))))