from PIL import Image

#im = Image.open("pexels-pixabay-20796.jpeg")

#print(im.size)

#im.show()

def load_pixel():

    im = Image.open("IMG_3226.jpg")
    y = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    z = '' 


    x = list(im.getdata())
    pixel = [int(sum(i)/3) for i in x]
    for i in range(len(pixel)):
        z += y[pixel[i]%len(y)]
        if i % im.size[0] == 0:
            print(z)
            z = ''

print(load_pixel())
