from bluedot import BlueDot
# The signal.signal() function allows defining custom handlers to be executed when a signal is received.
from signal import pause
# import PWMLED module from gpiozero library to brightness/color control RGB LED
from gpiozero import PWMLED

# RGB LED
greenLed = PWMLED(13)  # initialize GPIO13 as a LED pin
redLed = PWMLED(19)  # initialize GPIO19 as a LED pin
blueLed = PWMLED(26)  # initialize GPIO26 as a LED pin

# Create 10 virtual bluedot buttons side by side, by setting the number of cols to 2 and rows to 5
bd = BlueDot(cols=2, rows=5)
bd[0, 0].color = (255, 255, 255)  # On (R, G, B) >> White
bd[0, 0].square = True  # On (square button)
bd[0, 0].border = True  # On (border around button)
bd[1, 0].color = (0, 0, 0)  # Off (R, G, B) >> Black
bd[1, 0].square = True  # Off (square button)
bd[1, 0].border = True  # Off (border around button)
bd[0, 1].color = (255, 255, 255)  # White (R, G, B) >> White
bd[0, 2].color = (255, 0, 0)  # Red (R, G, B) >> Red
bd[0, 3].color = (0, 255, 0)  # Green (R, G, B) >> Green
bd[0, 4].color = (0, 0, 255)  # Blue (R, G, B) >> Blue
bd[1, 1].color = (0, 255, 255)  # Cyan (R, G, B) >> Cyan
bd[1, 2].color = (255, 0, 150)  # Magenta (R, G, B) >> Magenta
bd[1, 3].color = (255, 255, 0)  # Yellow (R, G, B) >> Yellow
bd[1, 4].color = (255, 102, 0)  # Yellow (R, G, B) >> Orange
#bd[1, 4].visible = False  # Will hide the last button, only 9 are needed.


# Callback functions if a button is pressed
def on_button(pos):
    print("On button is pressed")
    redLed.value = 1  # full brightness
    greenLed.value = 1  # full brightness
    blueLed.value = 1  # full brightness

def off_button(pos):
    print("Off button is pressed")
    redLed.value = 0  # off
    greenLed.value = 0  # off
    blueLed.value = 0  # off

# Callback functions if a slider is used
# The BlueDotPosition.x property returns a value from -1 (far down) to 1 (far up).
# Using this value you can create a slider (Dimmer) which goes vertically through the middle:
def set_bright_white(pos):
    print("White brightness slider is being sweeped")
    brightness = (pos.y + 1) / 2
    redLed.value = brightness
    greenLed.value = brightness
    blueLed.value = brightness

def set_bright_red(pos):
    print("Red brightness slider is being sweeped")
    brightness = (pos.y + 1) / 2
    redLed.value = brightness
    greenLed.value = 0
    blueLed.value = 0

def set_bright_green(pos):
    print("Green brightness slider is being sweeped")
    brightness = (pos.y + 1) / 2
    redLed.value = 0
    greenLed.value = brightness
    blueLed.value = 0

def set_bright_blue(pos):
    print("Blue brightness slider is being sweeped")
    brightness = (pos.y + 1) / 2
    redLed.value = 0
    greenLed.value = 0
    blueLed.value = brightness

def set_bright_cyan(pos):
    print("Cyan brightness slider is being sweeped")
    brightness = (pos.y + 1) / 2
    redLed.value = 0
    greenLed.value = brightness
    blueLed.value = brightness

def set_bright_magenta(pos):
    print("Magenta brightness slider is being sweeped")
    brightness = (pos.y + 1) / 2
    redLed.value = brightness
    greenLed.value = 0
    blueLed.value = brightness * (1 / 255) * 150

def set_bright_yellow(pos):
    print("Yellow brightness slider is being sweeped")
    brightness = (pos.y + 1) / 2
    redLed.value = brightness
    greenLed.value = brightness
    blueLed.value = 0

def set_bright_orange(pos):
    print("Yellow brightness slider is being sweeped")
    brightness = (pos.y + 1) / 2
    redLed.value = brightness
    greenLed.value = brightness * (1 / 255) * 102
    blueLed.value = 0

while True:
    # The Infinite while loop will monitor for Blue Dot button presses and button sweeps
    # and will run the needed callback function.
    # bd.when_pressed = button_pressed
    bd[0, 0].when_pressed = on_button
    bd[1, 0].when_pressed = off_button
    bd[0, 1].when_moved = set_bright_white
    bd[0, 2].when_moved = set_bright_red
    bd[0, 3].when_moved = set_bright_green
    bd[0, 4].when_moved = set_bright_blue
    bd[1, 1].when_moved = set_bright_cyan
    bd[1, 2].when_moved = set_bright_magenta
    bd[1, 3].when_moved = set_bright_yellow
    bd[1, 4].when_moved = set_bright_orange

    # Cause the process to sleep until a signal is received;
    # the appropriate handler will then be called. Returns nothing.
    pause()
