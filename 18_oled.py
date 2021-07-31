# require library - sudo pip3 install adafruit-circuitpython-ssd1306
from board import SCL, SDA
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
import time

i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3C)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Load default font.
font = ImageFont.load_default()

# Draw Some Text
text = "Hello World!"
draw.text(
    (0, 0),
    text,
    font=font,
    fill=255,
)

# Display image
oled.image(image)
oled.show()