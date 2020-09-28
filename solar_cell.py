import RPi.GPIO as GPIO
import time

filename = "/home/pi/solar_cell_reading"

#Setting the configuration as board instead of BCM
GPIO.setmode(GPIO.BOARD)

#Setting the pins in which the 8 bit output will come
GPIO.setup(3, GPIO.IN)
GPIO.setup(5, GPIO.IN)
GPIO.setup(8, GPIO.IN)
GPIO.setup(10, GPIO.IN)
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)

#Setting the pin in which the ALE(Address Latch Enable would be set)
GPIO.setup(38, GPIO.OUT)

#Setting the Address Latch to IN0 according to the clock cycle
GPIO.output(38, GPIO.HIGH)
time.sleep(0.5)
GPIO.output(38, GPIO.LOW)

while True:
    #Opening the file in which the readings of the solar cell need to be stored
    f = open(filename, "w")
    i = GPIO.input(3)*128 + GPIO.input(5)*64 + GPIO.input(8)*32+GPIO.input(10)*16+GPIO.input(11)*8+GPIO.input(12)*4+GPIO.input(13)*2+GPIO.input(15)*1
    #Digital output, needs to be converted to output voltage
    #i = i* 5/256
    #To get the current reading, we need to use the formula V=IR
    print(i)
    f.write(str(i))
    time.sleep(2)
