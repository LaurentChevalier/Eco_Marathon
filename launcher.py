import time
import serial
import os
import RPi.GPIO as GPIO


def readAndSave(n):
    print "usart running"
    path="/home/pi/Desktop/mesures"+str(n)+".csv"
    f = open(path,"w")
    port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=3.0)
    run=True
    GPIO.output(2,True)
    f.write("nouvelles mesures\n")
    while(run):
        recv= port.read(13)
        f.write(recv)
        print recv
        if (GPIO.input(3)==0):
            run=False
    f.close
    port.close()
    while (GPIO.input(3)==0):
        time.sleep(0.1)
    print "usart off"
    return

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(3,GPIO.IN)
    GPIO.setup(2,GPIO.OUT)

    n=1

    while True:
        GPIO.output(2,True)
        if (GPIO.input(3)==0):     
            while (GPIO.input(3)==0):
                time.sleep(0.1)
            readAndSave(n)
            n=n+1
            print n
        time.sleep(0.25)
        GPIO.output(2,False)
        time.sleep(0.25)
    return

main()
        
