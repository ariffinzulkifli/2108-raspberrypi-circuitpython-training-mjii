import board
import busio
import digitalio

import adafruit_rfm9x

RADIO_FREQ_MHZ = 923.0

CS = digitalio.DigitalInOut(board.D25)
RESET = digitalio.DigitalInOut(board.D17)

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

print("Waiting for packets...")

while True:
    packet = rfm9x.receive(timeout=5.0)
    
    if packet:
        print(packet)

        print("Received (raw bytes): {0}".format(packet))

        packet_text = str(packet, 'ascii')
        print("Received (ASCII): {0}".format(packet_text))

        rssi = rfm9x.last_rssi
        print("Received signal strength: {0} dB".format(rssi))

        print()
        