'''
Created on 25-08-2017

@author: instala
'''

import cv2

#cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False
    
rval, frame = vc.read()
success, image = vc.read()
cv2.imwrite("/tmp/img/image2.png", image)