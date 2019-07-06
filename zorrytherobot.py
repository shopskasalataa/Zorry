from gpiozero import Robot
import RPi.GPIO as gpio
import time
zorry = Robot(left=(4,17), right=(27,22))
while True:
    key = input()
    if key == '8':
        print('I\'m moving forward')
        zorry.forward(0.5)
    elif key == '2':
        print('I\'m moving backwards')
        zorry.backward(0.3)
    elif key == '4':
        print('I\'m moving left')
        zorry.left(0.4)
        zorry.right(0.3)
    elif key == '6':
        print('I\'m moving right')
        zorry.right(0.4)
        zorry.left(0.3)
    else:
        print('stop')
        zorry.stop()
        break
gpio.cleanup()
