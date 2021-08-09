# backgrounder with alpha channel

"""
from PIL import Image
png = Image.open('1.png').convert('RGBA')
background = Image.new('RGBA', png.size, (246,246,246))
alpha_composite = Image.alpha_composite(background, png)
alpha_composite.save('1.png')
"""

#numpy Segmentation

"""
import cv2
import numpy as np 

img=cv2.imread("img.png")
X,Y = np.where(np.all(img != [0,0,0],axis=2))
img[X,Y]=[255,255,255]
cv2.imwrite("img1.png",img)
"""



###convert image to jpg from png
"""
from PIL import Image
img=Image.open("img1.png")
rgb_im = img.convert('RGB')
rgb_im.save('img1.jpg')
"""



#alpha channel conversion

import cv2
import numpy as np
img=cv2.imread("1.jpg")
b_channel, g_channel, r_channel = cv2.split(img)

alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255 #creating a dummy alpha channel image.
print(alpha_channel)
img_BGRA = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))

cv2.imwrite("a.jpg",img_BGRA)


