## Mosquito Shooter

Nothing here so far

## Test Script
To test videostream clone into the repo and run  `python3 cv2_test.py` 

To terminate the program press 'q' on the keyboard

## Recognition Test

This program will try to make out faces, as well as eyes. Depending on hardware speed there might some lag. To run `cd` into the project directory and run `python Recognition_Test.py` 

## Mosquito approach 

To detect Mosquitoes a haar cascade object recognition model might not be the best solution. Instead it should be easier to apply a Background mask and do some denoising. 

Ich hab gerade gemerkt, dass das eine dumme Idee ist bei so einem Stream ist viel zu viel Noise und das wuerde wahrscheinlich nur vor einer Weissen Wand funktionieren, was auch der Himmel sein koennte, aber da ist irgendwie immer noch zu viel Noise, die ich vielleicht noch mit besseren Noise removal algorithmen wegkriegen koennte aber dazu hab ich gerade kein Bock.  
## Transforming picture coordinates to Laser movement

Hab ich grade kein Bock mir Gedanken zu mache aber irgedwie vielleicht mit tracking markern und dann
irgendwie umrechnen keine Ahnung
