from PIL import Image
import random

img = Image.open("img.png")
random.seed("123456")

w, h = img.size
pxs = []
for x in range(w):
    for y in range(h):
        pxs.append(img.getpixel((x, y)))

idx = list(range(len(pxs)))
random.shuffle(idx)

out = list(range(len(pxs)))
cur = 0
for i in idx:
    out[i] = pxs[cur]
    cur += 1
pxs = out

outImg = Image.new("RGB", img.size)
pxIter = iter(pxs)
for x in range(w):
    for y in range(h):
        outImg.putpixel((x, y), pxIter.__next__())
    outImg.save("unscrambled.png")
