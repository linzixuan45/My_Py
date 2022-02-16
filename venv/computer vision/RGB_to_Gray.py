from PIL import Image
import numpy as np

import os
input_dir = 'images/RGB/'
out_dir = 'images/Gray/'

a = os.listdir(input_dir)
for i in a:
    print(i)
    I = Image.open(input_dir+i)
    O = I.convert('L',dither=0)
    O.save(out_dir+i)