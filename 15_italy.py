from PIL import Image
im = Image.open("Data/wire.png")
print(im.size)
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
out = Image.new('RGB', [100, 100])
x = -1
y = 0
p = 0
d = 200
while d/2 > 0:
    for position in delta:
        steps = int(d / 2)
        # print(steps)
        for s in range(steps):
            x, y = x + position[0], y + position[1]
            # print(x, y)
            out.putpixel((x, y), im.getpixel((p, 0)))
            p += 1
        d -= 1
out.save('Data/15LevelImage.jpg')
