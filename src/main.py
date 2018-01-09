# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 15:27:42 2017
tel:13564180096
@author: bob.lee
"""
import cv2
import os
from src.face import Face
from src.idNumber import Number
path = os.path.join(os.path.dirname(__file__)) + '/haarcascade_frontalface_default.xml'


class Main(object):
    def __init__(self, image_path):
        self.image_path = image_path

    def main(self):
        image = cv2.imread(self.image_path)
        image_face = Face(image, path).face_location()
        text = Number(image).number()
        return image_face, text
