## Laser Shooter
To use the program ssh into the Rasperry Pi, run `cd 'Servo Movement'` and then start the server by running `python server.py`. Then on the computer cd into the `FaceRecogniton` Directory and run `python Recognition_Test.py`, then run `python Tracking.py` on the Rasperry Pi again.   

## Test Script
To test videostream clone into the repo and run  `python3 cv2_test.py` 

To terminate the program press 'q' on the keyboard

## Recognition Test

This program will try to make out faces, as well as eyes. Depending on hardware speed there might some lag. To run `cd` into the FaceRecogniton directory and run `python Recognition_Test.py`

## Transforming picture coordinates to Laser movement
SSH into your Rasperry Pi `cd` into the Servo Controll Directory and run `sudo pigpiod` to set up hardwaregenerated pwm signals. Then to test the servo run `python3 Servo_test.py`

## Server Communication
The transport of data happens between the pi and a more powerful computer. The server and client programms can be found in the `Communication` Directory but are not called from there. The client program is startet at the same time as the FaceRecogniton starts. The server is started together with the Servo Movement program. 

