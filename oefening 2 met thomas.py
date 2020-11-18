#!/usr/bin/env python
"""
Info about our project comes here
"""

# IMPORTS
from gpiozero import Button




__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Development"

# I/O CONFIG
IP = '169.254.129.229'
BUTTON_UP = Button(pin =4, pin_factory=IP)
BUTTON_DOWN = Button(pin=5,pin_factory=IP)


def main():
    while True:
        counter = 0
        if BUTTON_UP.is_pressed:
            counter += 1
            print(counter)
        if BUTTON_DOWN.is_pressed:
            counter -= 1
            print(counter)


if __name__ == '__main__':  # code to execute if called from command-line
    main()








