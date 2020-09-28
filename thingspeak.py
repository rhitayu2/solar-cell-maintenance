import httplib
import urllib
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# Putting the Write API Key in the variable
key = THING_SPEAK_KEY

"""
Setting up the LDR module for checking the intensity of light apart from
solar panel
"""
#Hard coding the Ouput pin as pin no.7
pin_to_circuit = 7

def ldr_reading ():
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
            GPIO.cleanup()
    return count/1e3
    GPIO.cleanup()

"""
The part of the code where ThingSpeak sends the data regarding the Solar Cell

"""



def ts_ldr():
    count = 0
    sum_ldr = 0
    for i in range(5):
        sum_ldr += ldr_reading()
        print(ldr_reading())
    #The case where there isn't apt sunlight, return 0, indicating nothing
    #wrong with the solar cell
    if (sum_ldr <= 36):
        return 0

    #The case where there is apt sunlight, return 1, indicating the solar
    #cell isn't producing the voltage
    else:
        return 1



def ts_check_against_ldr(intensity):
    x = ts_ldr() * intensity
    if (x == 0):
        print("Not enough sunlight")

    elif (x > 0 ):
        print("Sunlight present, there would be some maintenance issue")

    params = urllib.urlencode({'field2': x, 'key':key })
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print("LDR Intensity: {}".format(x))
        #print response.status, response.reason
        data = response.read()
        conn.close()
    except:
        print "connection failed"


def ts_graph():
    while True:
        #Open the file solar_cell_reading
        temp = int(open('/home/pi/solar_cell_reading').read()) 
        #Hypothetically providing the threshold as 5
        threshold = 300
        params = urllib.urlencode({'field1': temp, 'key':key })
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print ("Solar Panel: {}".format(temp))
            #print response.status, response.reason
            data = response.read()
            conn.close()
        except:
            print "connection failed"
        if(temp <= threshold):
            ts_check_against_ldr(temp)

def main():
    while True:
        ts_graph()

if __name__ == "__main__":
    main()
