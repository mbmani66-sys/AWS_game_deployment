apple = Actor("apple")

def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = 300
    apple.y = 200
place_apple()

def on_mouse_down(pos):
    print("Good shot!")
    place_apple()

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shot!")
        place_apple()
    else:
        print("You missed!")
        quit()
from random import randint

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)
    