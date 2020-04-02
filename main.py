import board
import adafruit_ws2801 as ws2801
import RPi.GPIO as GPIO
import time

led = 17
K1 = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(K1, GPIO.OUT)

GPIO.output(K1, GPIO.LOW)

#for i in range(10):
#    GPIO.output(led, GPIO.HIGH)
#    time.sleep(0.2)
#    GPIO.output(led, GPIO.LOW)
#    time.sleep(0.2)
time.sleep(0.2)

darkred = 0x100000

pixels = ws2801.WS2801(board.SCLK, board.MOSI, 41, brightness=1.0, auto_write=True)

pixels.fill((0x80, 0x30, 0x10))
pixels.show()
time.sleep(5)

pixels.fill((0x10, 0x30, 0x80))
pixels.show()
time.sleep(5)

GPIO.cleanup()