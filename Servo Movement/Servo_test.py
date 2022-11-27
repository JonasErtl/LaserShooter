from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

#Declaring servo pin 
servo = Servo(14, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

while True:
    servo.min()
    sleep(1)
    servo.mid()
    sleep(1)
    servo.max()
    sleep(1)
servo.Value = None;
