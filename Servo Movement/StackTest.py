from gpiozero import Servo
from time import sleep 
from gpiozero.pins.pigpio import PiGPIOFactory


#Declaring Hardware generated PWM signal
factory = PiGPIOFactory()

#Declaring Servos

bottomServo = Servo(14, pin_factory=factory)
topServo = Servo(15, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

sleepTime = 0.8

while True:
    topServo.min()
    sleep(sleepTime)
    bottomServo.min()
    sleep(sleepTime)
    topServo.max()
    sleep(sleepTime)
    bottomServo.max()
    sleep(sleepTime)
bottomServo.value = None;
topServo.value = None;

