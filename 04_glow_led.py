import time
import board
import pwmio
 
led = pwmio.PWMOut(board.D12, frequency=5000, duty_cycle=0)

print("breathing light!")
 
while True:
    for i in range(100):
        if i < 50:
            led.duty_cycle = int(i * 2 * 65535 / 100)
        else:
            led.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)
        time.sleep(0.01)