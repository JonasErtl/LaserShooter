#Approach to detetct Mosquitoes using a background Mask and denoising

import numpy as np
import cv2
  
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3));
  
# creating object
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG();
  
# capture frames from a camera 
cap = cv2.VideoCapture(0);
while(1):
    # read frames
    ret, img = cap.read();
      
    # apply mask for background subtraction
    fgmask = fgbg.apply(img);
      
    # with noise frame
#    cv2.imshow('GMG noise', fgmask);
      
    # apply transformation to remove noise
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel);
      
    # after removing noise
    cv2.imshow('GMG', fgmask);
      
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release();
cv2.destroyAllWindows();
