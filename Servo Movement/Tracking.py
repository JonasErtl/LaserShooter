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

def conversion_func(index, iszero):
    if iszero == True:
        try:
            return ((320-float(index))*3.125/1000)
        except:
            pass
    else:
        try:
            return ((240-float(index))*4.1666666/1000)
        except:
            pass


while True:
    file1 = open("file.txt","r")
    lis = file1.read()
    a = lis.strip().split(',')
    bottomServo.value = conversion_func(a[0], True)
    topServo.value = conversion_func(a[-1], False)
bottomServo.value = None;
topServo.value = None;

