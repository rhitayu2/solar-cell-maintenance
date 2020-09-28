#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pin_to_circuit = 7

def rc_time ():
    count = 0
  
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(7, GPIO.IN)
    init_time = time.time()  
    
    while (GPIO.input(7) == GPIO.LOW):
        count += 1
        if(time.time() - init_time >= 0.05):
            return count/1e3                
    return count/1e3

def main():
    try:
        while True:
            print(rc_time())
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()