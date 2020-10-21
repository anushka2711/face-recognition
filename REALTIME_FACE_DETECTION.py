# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:43:23 2020

@author: anush
"""

import cv2
import face_recognition

web_stream=cv2.VideoCapture(0)

all_face_location=[]
while True:
    ret,current_frame= web_stream.read()
    small_current_frame= cv2.resize(current_frame,(0,0),fx=0.25,fy=0.25)
    all_face_location= face_recognition.face_locations(small_current_frame,model='hog')
    for index,current_image_location in enumerate(all_face_location):
        top,right,bottom,left=current_image_location
        top=top*4
        right=right*4
        bottom=bottom*4
        left=left*4
        print("pos of face {} is {}".format((index+1),current_image_location))
        cv2.rectangle(current_frame,(left,top),(right,bottom),(0,255,0),2)
    cv2.imshow("webcan video",current_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
web_stream.release()
cv2.destroyAllWindows() 
    
        
        
  
    
  
    
  
    
  
    
  
    
  
    
    
    