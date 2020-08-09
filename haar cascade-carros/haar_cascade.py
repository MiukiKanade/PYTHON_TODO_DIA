#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cv2

cascade_src = 'cars.xml'
video_src = 'Taiwan.mp4'

cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)

while True:
    ret, img = cap.read()
    img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.putText(img, 'Veiculo', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    
    cv2.imshow('video', img)
    key = cv2.waitKey(10)
    
    if key == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break

cv2.destroyAllWindows()

