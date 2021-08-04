import os
from PIL import Image, ImageChops
def trim(im):
     bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
     diff = ImageChops.difference(im, bg)
     diff = ImageChops.add(diff, diff, 2.0, -100)
     bbox = diff.getbbox()
     if bbox:
        return im.crop(bbox)
input_folder = 'images'

for img in os.listdir(input_folder):
    try:
        if img.endswith(('.jpg','.jpeg','.png')):
            img = os.path.join(input_folder,img)
            print('Processing ', img)
            
            im = Image.open(img)
            print(im.size)
            os.makedirs('results',exist_ok=True)
            img = img.split('/')[-1]
            trim(im).save('results/'+img)
    except:pass
