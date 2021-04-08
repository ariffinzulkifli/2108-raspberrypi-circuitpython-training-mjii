import board
import busio
import digitalio
import requests
import json

import adafruit_rfm9x

RADIO_FREQ_MHZ = 923.0

CS = digitalio.DigitalInOut(board.D25)
RESET = digitalio.DigitalInOut(board.D17)

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

def http_request(d):

    data = d.split(',', 3)

    if data[0] == 'fav':
        try:

            reqbody = {
                'device_developer_id': data[2],
                'data': json.loads(data[3])
            }

            req = requests.post(
                'https://apiv2.favoriot.com/v2/streams',
                timeout = 5,
                headers = {
                    'content-type': 'application/json',
                    'apikey': data[1]
                },
                data = json.dumps(reqbody)
            )

            res = json.loads(req.text)
            print(res)

            if res["statusCode"] == 20150:
                print("Successful to create data stream for device: " + data[2])
            else:
                print("Unsuccessful to create data stream. Error: " + res)
        
        except requests.exceptions.HTTPError as errh:
            print ('An Http Error occurred: ') + repr(errh)
        
        except requests.exceptions.ConnectionError as errc:
            print ('An Error Connecting to the API occurred: ') + repr(errc)
        
        except requests.exceptions.Timeout as errt:
            print ('A Timeout Error occurred: ') + repr(errt)
        
        except requests.exceptions.RequestException as err:
            print ('An Unknown Error occurred ') + repr(err)
    else:
        print("Not Favoriot-LoRa Data")
    print()


print('Waiting for packets...')

while True:
    packet = rfm9x.receive(timeout=5.0)
    
    if packet:
        packet_text = str(packet, 'ascii')
        print('Received (ASCII): {0}'.format(packet_text))

        rssi = rfm9x.last_rssi
        print('Received signal strength: {0} dB'.format(rssi))

        http_request(packet_text)