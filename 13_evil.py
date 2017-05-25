data = open('Data/evil2.gfx', 'rb').read()
types = ['jpg', 'png', 'gif', 'png', 'jpg']
print (data[2:60:5])
for i in range(5):
    open('Data/%d.%s' % (i, types[i]), 'wb').write(data[i::5])
