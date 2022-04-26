from PIL import Image, ImageDraw, ImageFont
import os
#from PIL import Image
from imageio import imread, imwrite
from scipy import misc
import numpy as np
import math

#в переменной cycle хранится количество изображений, которые нужно склеить. необходимо выбрать шаблон имени и запустить прогу. можно донастроить, чтобы отсчет начинался с 0, но мне лень 

cycle = 369

original_image = Image.open('Lorenz Attractor100.png')
images = list()
for z in range(100, cycle):
        tmp = Image.open('Lorenz Attractor'+('0'+str(z) if z <10 else str(z))+'.png')
        images.append(tmp)

original_image.save('Result.gif', append_images=images, loop=0, duration=50, save_all=True)
