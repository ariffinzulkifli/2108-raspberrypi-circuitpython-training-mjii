import time
import board
import pwmio
from adafruit_motor import servo

pwm = pwmio.PWMOut(board.D5, duty_cycle=2 ** 15,  frequency=50)

servo = servo.Servo(pwm)
servo.angle = 90

time.sleep(5)

print("servo motor sweeping!")

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        servo.angle = angle
        time.sleep(0.05)