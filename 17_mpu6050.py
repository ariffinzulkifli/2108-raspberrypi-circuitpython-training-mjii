# require library - pip3 install adafruit-circuitpython-mpu6050
import time
import board
import adafruit_mpu6050

i2c = board.I2C()
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    acr = mpu.acceleration
    
    print("Acceleration: X: " + "%.2f"%acr[0] + ", Y: " + "%.2f"%acr[1] + ", Y: " + "%.2f"%acr[2] + " m/s^2")
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f degrees/s"%(mpu.gyro))
    print("Temperature: %.2f C"%mpu.temperature)
    print("")
    time.sleep(1)