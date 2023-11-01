# -*- coding: utf-8 -*-
"""OCR_in_Auto.

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RHDkgx30_envlYc_LWyzfHPZ31fYwaNt

Here we going to build OCR for automation number plate recogination

We would be using yolo r
"""

!pip install easyocr

import easyocr
import matplotlib.pyplot as plt
import cv2
import time
import numpy as np

reader = easyocr.Reader(['en'], gpu=True)
vid = cv2.VideoCapture("ocr.mp4") # this is for input video
#vid = cv2.VideoCapture(0) this is for webcam

# now we are going to implement the frame skipping, this is so that ocr doesn't hold back our detector
skip_frame = True

while(True):
  a = time.time()  #setting our intial time
  ret, img = vid.read()
  
  #now we are going to convert our image into grayscale 
  #gray = cv2.cvtColor(img, cv2.Color_RGB2GRAY)
  gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
  result = reader.readtext(gray)
  text = " "  #creating empty container

  for res in result:
    text += res[1] + " "
  cv2.putText(img, text, (50,70,), cv2.FONT_HERSHEY_SIMPLEX, 1, (50,50,255), 2)

  #specifying frame rate
  b = time.time()
  fps = 1/(b-a)
  #so here we woulding to explain frame per second
  #cv2.rectangle((20,25), (127, 25), [85, 45,255], 38)
  cv2.putText(img, text, (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (50,50,255), 2)
  plt.imshow(img)

  #if cv2.waitKey(1) & 0xFF == ord('q'):
    #  break 
  print(fps)
  print(text)    

# cv2.cvtColor(ave_image,cv2.COLOR_BGR2RGB)