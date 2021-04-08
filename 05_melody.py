import time
import board
import pulseio

TONE_FREQ = [ 262,  # C4
              294,  # D4
              330,  # E4
              349,  # F4
              392,  # G4
              440,  # A4
              494 ] # B4

buzzer = pulseio.PWMOut(board.D15, variable_frequency=True)

buzzer.frequency = TONE_FREQ[0]
buzzer.duty_cycle = 2**15  # 32768 value is 50% duty cycle, a square wave.

print("play melody!")

while True:
    for i in range(len(TONE_FREQ)):
        buzzer.frequency = TONE_FREQ[i]
        time.sleep(0.5)
    for i in range(len(TONE_FREQ)-1, -1, -1):
        buzzer.frequency = TONE_FREQ[i]
        time.sleep(0.5)