from gpiozero import Servo
from time import sleep 
from gpiozero.pins.pigpio import PiGPIOFactory

#Declaring Hardware generated PWM signal
factory = PiGPIOFactory()

#Declaring Servos
bottomServo = Servo(14, pin_factory=factory)
topServo = Servo(15, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

#Declaring Servo Movement variables
x_value = 1.0 #Only to be used with bottomServo
y_value = -1.0 #Only to be used with topServo

sleepTime = 0.3

while True:
    bottomServo.value = x_value
    topServo.value = y_value
bottomServo.value = None;
topServo.value = None;

