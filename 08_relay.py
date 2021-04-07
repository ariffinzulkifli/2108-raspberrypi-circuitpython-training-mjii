import time
import board
import digitalio
 
print("relay!")
 
relay = digitalio.DigitalInOut(board.D5)
relay.direction = digitalio.Direction.OUTPUT
 
while True:
    relay.value = True
    time.sleep(0.5)
    relay.value = False
    time.sleep(0.5)