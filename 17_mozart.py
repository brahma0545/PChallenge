import numpy as np
from PIL import Image

image = Image.open("Data/mozart.gif")
# print(max(enumerate(image.histogram()), key=lambda x: x[1]))
tmp = image.copy()
tmp.frombytes(bytes([195] * (tmp.height * tmp.width)))
# tmp.show()
# print([60] * (tmp.height * tmp.width))

# print(image.histogram())
# for i, elt in enumerate(image.histogram()):
#     print(i, elt)

print([x for x in image.histogram() if x % image.height == 0 and x != 0])
print(image.histogram().index(2400))
shifted = [bytes(np.roll(row, -row.tolist().index(195)).tolist()) for row in np.array(image)]
print(shifted)
Image.frombytes(image.mode, image.size, b"".join(shifted)).show()
