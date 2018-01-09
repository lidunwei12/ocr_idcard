# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 15:27:42 2017
@author: bob.lee
"""
import cv2
from PIL import Image
import re
import os
import pytesseract
TEMP_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'temp'))
if not os.path.isdir(TEMP_PATH):
    os.mkdir(TEMP_PATH)


def number_find(content):
    re_words = re.compile("[X0-9]+")
    result = re.findall(re_words, content)
    result = "".join(result)
    return result


def location(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 灰度化图像
    image_turn = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 35, 35)
    image_turn = cv2.medianBlur(image_turn, 3)
    (rew, image_turn) = cv2.threshold(image_turn, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # 图像反转
    image_dilate = cv2.dilate(image_turn, None, iterations=15)
    image_erode = cv2.erode(image_dilate, None, iterations=12)
    (rew, image_back_binary) = cv2.threshold(image_erode, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    (rew, handle_image) = cv2.threshold(image_back_binary, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    img_fc, contours, hierarchy = cv2.findContours(handle_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    im_bottom = []
    for i in range(len(contours)):
        if cv2.contourArea(contours[i]) < 10000:
            continue
        x, y, w, h = cv2.boundingRect(contours[i])
        if w/h < 0.3 or h/w >= 0.3:
            continue
        # print( cv2.contourArea(contours[i]))
        im_bottom.append([x, y, w, h])
        # image = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return image, im_bottom


def ocr_result(image, content):
    image = image[content[1]:content[1]+content[3], content[0]:content[0]+content[2], :]
    image_text = Image.fromarray(image)
    text = pytesseract.image_to_string(image_text)
    return text


def number(img):
    image, content = location(img)
    result_text = ''
    for i in range(len(content)):
        text = ocr_result(image, content[i])
        result = number_find(text)
        if len(result) == 18:
            result_text = result
            break
    return result_text


class Number(object):

    def __init__(self, image):
        self.image = image

    def number(self):
        image, content = location(self.image)
        result_text = ''
        for i in range(len(content)):
            text = ocr_result(image, content[i])
            result = number_find(text)
            if len(result) == 18:
                result_text = result
                break
        return result_text
