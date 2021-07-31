from time import sleep
import sys
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

while True:
    print("Hold a tag near the reader")
    id, text = reader.read()
    print("ID: %s" % (id))
    sleep(5)