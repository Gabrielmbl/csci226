from sense_hat import *
from time import sleep
from random import choice

sense = SenseHat()
sense.clear()

# Just return the actions we are interested in
def wait_for_move():
  while True:
    e = sense.stick.wait_for_event()
    if e.action != ACTION_RELEASED:
      return e

w = (150, 150, 150)
g = (0, 255, 0)
r = (255, 0, 0)
e = (0, 0, 0)

arrowUp = [
e,e,e,w,w,e,e,e,
e,e,w,w,w,w,e,e,
e,w,e,w,w,e,w,e,
w,e,e,w,w,e,e,w,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e
]

arrowUpRed = [
e,e,e,r,r,e,e,e,
e,e,r,r,r,r,e,e,
e,r,e,r,r,e,r,e,
r,e,e,r,r,e,e,r,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e
]

arrowUpGreen = [
e,e,e,g,g,e,e,e,
e,e,g,g,g,g,e,e,
e,g,e,g,g,e,g,e,
g,e,e,g,g,e,e,g,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e
]

arrowR = [
e,e,e,e,w,e,e,e,
e,e,e,e,e,w,e,e,
e,e,e,e,e,e,w,e,
w,w,w,w,w,w,w,w,
e,e,e,e,e,e,w,e,
e,e,e,e,e,w,e,e,
e,e,e,e,w,e,e,e,
e,e,e,w,e,e,e,e
]

arrowRRed = [
e,e,e,e,r,e,e,e,
e,e,e,e,e,r,e,e,
e,e,e,e,e,e,r,e,
r,r,r,r,r,r,r,r,
e,e,e,e,e,e,r,e,
e,e,e,e,e,r,e,e,
e,e,e,e,r,e,e,e,
e,e,e,r,e,e,e,e
]

arrowRGreen = [
e,e,e,e,g,e,e,e,
e,e,e,e,e,g,e,e,
e,e,e,e,e,e,g,e,
g,g,g,g,g,g,g,g,
e,e,e,e,e,e,g,e,
e,e,e,e,e,g,e,e,
e,e,e,e,g,e,e,e,
e,e,e,g,e,e,e,e
]

arrowL = [
e,e,e,w,e,e,e,e,
e,e,w,e,e,e,e,e,
e,w,e,e,e,e,e,e,
w,w,w,w,w,w,w,w,
e,w,e,e,e,e,e,e,
e,e,w,e,e,e,e,e,
e,e,e,w,e,e,e,e,
e,e,e,e,w,e,e,e
]

arrowLRed = [
e,e,e,r,e,e,e,e,
e,e,r,e,e,e,e,e,
e,r,e,e,e,e,e,e,
r,r,r,r,r,r,r,r,
e,r,e,e,e,e,e,e,
e,e,r,e,e,e,e,e,
e,e,e,r,e,e,e,e,
e,e,e,e,r,e,e,e
]

arrowLGreen = [
e,e,e,g,e,e,e,e,
e,e,g,e,e,e,e,e,
e,g,e,e,e,e,e,e,
g,g,g,g,g,g,g,g,
e,g,e,e,e,e,e,e,
e,e,g,e,e,e,e,e,
e,e,e,g,e,e,e,e,
e,e,e,e,g,e,e,e
]

arrowDown = [
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
w,e,e,w,w,e,e,w,
e,w,e,w,w,e,w,e,
e,e,w,w,w,w,e,e,
e,e,e,w,w,e,e,e
]

arrowDownRed = [
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
r,e,e,r,r,e,e,r,
e,r,e,r,r,e,r,e,
e,e,r,r,r,r,e,e,
e,e,e,r,r,e,e,e
]

arrowDownGreen = [
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
g,e,e,g,g,e,e,g,
e,g,e,g,g,e,g,e,
e,e,g,g,g,g,e,e,
e,e,e,g,g,e,e,e
]

score = 0

sense.show_message("Joystick to correct direction", scroll_speed=0.05, text_colour=[100,100,100])

for turns in range(10):
  
    last_dir = dir
    while dir == last_dir:
        dir = choice([arrowUp, arrowDown, arrowR, arrowL])
        
    sense.set_pixels(dir)
    sleep(0.02)
    sense.clear()
    
  
    while True:
  
        e = wait_for_move()
    
        if e.direction == DIRECTION_UP and dir == arrowUp:
            sense.set_pixels(arrowUpGreen)
            score += 1
            sleep(1)
            sense.clear()
            sleep(0.75)
            break;
        elif e.direction == DIRECTION_UP and dir != arrowUp:   
            sense.set_pixels(arrowUpRed)
            sleep(1)
            sense.clear()
            sleep(0.75)
            break;
        elif e.direction == DIRECTION_DOWN and dir == arrowDown:
            sense.set_pixels(arrowDownGreen)
            score += 1
            sleep(1)
            sense.clear()
            sleep(0.75)
            break;
        elif e.direction == DIRECTION_DOWN and dir != arrowDown:
            sense.set_pixels(arrowDownRed)
            sleep(1)
            sense.clear()
            sleep(0.75)
            break;
        elif e.direction == DIRECTION_RIGHT and dir == arrowR:
            sense.set_pixels(arrowRGreen)
            score += 1
            sleep(1)
            sense.clear()
            sleep(0.75)
            break;
        elif e.direction == DIRECTION_RIGHT and dir != arrowR:
            sense.set_pixels(arrowRRed)
            sleep(1)
            sense.clear()
            sleep(0.5)
            break;
        elif e.direction == DIRECTION_LEFT and dir == arrowL:
            sense.set_pixels(arrowLGreen)
            score += 1
            sleep(1)
            sense.clear()
            sleep(0.75)
            break;
        elif e.direction == DIRECTION_LEFT and dir != arrowL:
            sense.set_pixels(arrowLRed)
            sleep(1)
            sense.clear()
            sleep(0.75)
            break;


      
sense.show_message("Score: " + str(score))       
