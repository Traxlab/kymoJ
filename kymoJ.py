from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt
import math

# Access all PNG files in directory
allfiles=os.listdir(os.getcwd())
imlist=[filename for filename in allfiles if  filename[-4:] in [".png",".PNG"]]


# Assuming all images are the same size, get dimensions of first image
w,h=Image.open(imlist[0]).size
N=len(imlist)

first= True
for im in imlist:
    temp=np.asarray(Image.open(im))
    temp = temp.astype('uint32')
    if first:
    	sumImage=temp
    	first=False
    else: 
    	sumImage+= temp

class Formatter(object):
    def __init__(self, im):
        self.im = im
    def __call__(self, x, y):
        z = self.im.get_array()[int(y), int(x)]
        return 'x={:.01f}, y={:.01f}, z={:.01f}'.format(x, y, z)


avgArray = sumImage/len(imlist)
first=True
devArray= avgArray
for im in imlist:
    temp=np.asarray(Image.open(im))
    temp = temp.astype('uint32')
    if first: 
        devArray= np.square(avgArray-temp)
        first= False
    else: 
        devArray += np.square(avgArray-temp)

devArray= np.sqrt(devArray/ len(imlist))
devImage= Image.fromarray(devArray.astype('uint8'))
#devImage.show()

avgImg = Image.fromarray(avgArray.astype('uint8'))
avgImg.save("average1.png")
#avgImg.show()
avgImg= Image.open("average1.png")
fig, ax = plt.subplots()
im = ax.imshow(avgImg, interpolation='none')
ax.format_coord = Formatter(im)
plt.show()



#avgImg= Image.open("average1.png")
# fig, ax = plt.subplots()
# im = ax.imshow(devImage, interpolation='none')
# ax.format_coord = Formatter(im)
# plt.show()



