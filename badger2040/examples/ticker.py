import time
import machine
import badger2040
from badger2040 import WIDTH

screen = badger2040.Badger2040()
screen.led(128)
screen.update_speed(badger2040.UPDATE_TURBO)

restart = False  # should sim be restarted

# We're going to keep the badger on, so slow down the system clock if on battery
badger2040.system_speed(badger2040.SYSTEM_SLOW)

rtc = machine.RTC()
display = badger2040.Badger2040()
display.led(128)
display.update_speed(badger2040.UPDATE_TURBO)
display.font("gothic")


# Set up the buttons
button_down = machine.Pin(badger2040.BUTTON_DOWN, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_up = machine.Pin(badger2040.BUTTON_UP, machine.Pin.IN, machine.Pin.PULL_DOWN)

button_a = machine.Pin(badger2040.BUTTON_A, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_b = machine.Pin(badger2040.BUTTON_B, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_c = machine.Pin(badger2040.BUTTON_C, machine.Pin.IN, machine.Pin.PULL_DOWN)

# import the time module
import time
  
# define the countdown func.
def countdown(t):
    
    while t:
        secs = t
        timer = '{:12d}'.format(secs)
        print(timer, end="\r")
        time.sleep(1)
        t += 1
        
  
# input time in seconds
t = 999

display.pen(0)
display.rectangle(0, 0, WIDTH, 16)
display.thickness(1)
display.pen(15)
badger.clear()
display.text(str(t),10,20)
screen.update_speed(badger2040.UPDATE_TURBO)
  
# function call
countdown(int(t))
