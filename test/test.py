# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 15:27:42 2017
tel:13564180096
@author: bob.lee
"""
import time
from PIL import Image
from src.main import Main
import os
TEMP_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'temp'))
if not os.path.isdir(TEMP_PATH):
    os.mkdir(TEMP_PATH)
time_start = time.time()
image_face, id_number = Main(TEMP_PATH+'/230103198602230916.jpg').main()
print(id_number)
color_gray_bin = Image.fromarray(image_face)
color_gray_bin.show()
print(time.time()-time_start)