import badger2040
import time

badger = badger2040.Badger2040()
# We're going to keep the badger on, so slow down the system clock if on battery
badger2040.system_speed(badger2040.SYSTEM_SLOW)


badger.update_speed(badger2040.UPDATE_TURBO)
badger.thickness(8)

# import the time module
  
# define the countdown func.
def countdown(t):
    
    while t:
        secs = t
        timer = '{:12d}'.format(secs)
        print(timer, end="\r")
        time.sleep(1)
        t += 1
       # display.text(str(t), 50, 20)
        badger.pen(0)
        badger.text(str(t), 40, 64,scale=1.7)
        badger.update()
        badger.pen(15)
        badger.clear()
       
      #  badger.clear()
      #  badger.update()

        
# input time in seconds
t = 000001


# function call
countdown(int(t))

