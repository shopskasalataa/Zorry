from gpiozero import Robot
# 
import RPi.GPIO as gpio
# този код е за да се контролират GPIO пиновете на Raspberry-то
import time
#импортва се модулът time
zorry = Robot(left=(4,17), right=(27,22))
#избираме пиновете, които ще използваме, за да свържем мотора с raspberry-то
while True:
    key = input()
#тук ще съхраняваме входа от клавиатурата
    if key == '8':
#ако е 8
        print('I\'m moving forward')
#извежда в конзолата, че се движи напред
        zorry.forward(0.5)
#роботът се придвижва напред 
    elif key == '2':
#ако е равно на 2
        print('I\'m moving backwards')
#извежда в конзолата, че се движи назад
        zorry.backward(0.3)
#роботът се придвижва назад 
    elif key == '4':
#ако е въведено 4
        print('I\'m moving left')
#за да завие робота наляво
        zorry.left(0.4)
#намаляваме скоростта с която се движи десния мотор
        zorry.right(0.3)
#
    elif key == '6':
#ако е въведено 6
        print('I\'m moving right')
#за да завие надясно
        zorry.right(0.4)
#намаляваме скоростта с която се движи левия мотор
        zorry.left(0.3)
#
    else:
        print('stop')
#в противен случай извежда стоп в конзолата
        zorry.stop()
#и роботът спира
        break
#цикълът приключва
gpio.cleanup()
#затваря стриймовете за да могат да бъдат използвани отново в друг код
