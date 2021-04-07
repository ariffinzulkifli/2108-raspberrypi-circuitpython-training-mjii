import adafruit_ssd1306
import board
import busio
from digitalio import DigitalInOut
 
spi = busio.SPI(board.SCLK, MOSI=board.MOSI, MISO=board.MISO)
dc_pin = DigitalInOut(board.D13)    # any pin!
reset_pin = DigitalInOut(board.D19) # any pin!
cs_pin = DigitalInOut(board.D6)    # any pin!
 
oled = adafruit_ssd1306.SSD1306_SPI(128, 32, spi, dc_pin, reset_pin, cs_pin)

oled.fill(0)
oled.show()