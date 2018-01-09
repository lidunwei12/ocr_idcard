# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 15:27:42 2017

@author: bob.lee
"""
import cv2


class Face(object):

    def __init__(self, image, xml):
        self.image = image
        self.xml = xml

    def face_location(self):
        image = self.image
        face_path = self.xml
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(face_path)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.15,
            minNeighbors=5,
            minSize=(5, 5),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        # content = sorted(faces, key=faces[2]*faces[3], reverse=True)
        area = []
        for (x, y, w, h) in faces:
            area.append(w*h)
            # cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)
            # cv2.circle(image, (int((x + x + w) / 2), int((y + y + h) / 2)), int(w / 2), (0, 255, 0), 2)
        if len(faces) != 0:
            faces = faces[area.index(max(area))]
            image = image[faces[1]:faces[1]+faces[3], faces[0]:faces[0]+faces[2], :]
        return image
