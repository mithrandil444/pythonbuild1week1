#!/usr/bin/env python
"""
Je laat een LED aangaan, na 5 seconden schakelt deze LED terug uit. Na 2 seconden gaat deze terug aan, na 2 seconden
ook weer uit. Dit herhaal je 5 keer waarna de led in een blink toestand blijft
"""


from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
import time



__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Development"


button = Button(2)
IP = PiGPIOFactory(host='svendv')
led = LED(pin=17, pin_factory=IP)


def main():
    led.source = button


if __name__ == '__main__':  # code to execute if called from command-line
    main()
