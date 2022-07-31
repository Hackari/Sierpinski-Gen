from PIL import Image, ImageDraw
from io import BytesIO
import random
save_kwargs = {
    "format": "GIF",
    "save_all": True,
    "duration": 1,
    "loop": False,
}
frames = []
a = 0
x = random.randint(0,499)
y = random.randint(0,432)
c = 50000
listx = [0, 250, 499]
listy = [432, 0, 432]
img = Image.new('P', (500, 433), color = 'black')
ImageDraw.Draw(img).line((0,432,250,0),fill='white',width=1)
ImageDraw.Draw(img).line((0,432,499,432),fill='white',width=1)
ImageDraw.Draw(img).line((499,432,250,0),fill='white',width=1)
pixels = img.load()
while a < c:
    b = random.randint(0,2)
    x = (x+listx[b])/2
    y = (y+listy[b])/2
    pixels[x,y] = 128
    a += 1
    print(a)
    frames.append(img.copy())
byteframes = []
for f in frames:
    byte = BytesIO()
    byteframes.append(byte)
    f.save(byte, format="GIF")
imgs = [Image.open(byteframe) for byteframe in byteframes]
imgs[0].save("goobod.gif", append_images=imgs[1:], **save_kwargs)
img.save('hello.png')
print('--END--')
img.show()
