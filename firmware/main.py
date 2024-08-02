#import configs 
from config.interface import I2C as i2c
from config.interface import SPI as spi
from config.interface.comms.WLAN import config as wlan_config

from config.userinput.userinput_analog.OnboardTouchPad import config as moisture
from config.pixel.monochrome import SSD1327 as ssd
from config.environment.moist import SHTC3 as shtc3
from config.environment.light import SI1145 as si1145
from config.application.remote.Mqtt import config as mqtt_config

#import fw
from firmware.interface.I2C import I2C
from firmware.interface.SPI import SPI
from firmware.interface.comms.WLAN import WLAN

from firmware.userinput.userinput_analog.OnboardTouchPad import OnboardTouchPad
from firmware.application.remote.Mqtt import Mqtt
from firmware.pixel.monochrome.SSD1327 import SSD1327
from firmware.environment.moist.SHTC3 import SHTC3
from firmware.environment.light.SI1145 import SI1145

#other imports
from machine import deepsleep, mem32
from time import sleep, sleep_us
    
#mqtt pub helper
def mqtt_masspub(client, data):
    for values in data:
        if values['type'] == 'float':
            message = b"%.2f" % values['value']
        elif values['type'] == 'bool':
            message = b"%s" % str(values['value']).encode('utf-8')
        client.main(hook='publish', publish_args={'topic': f"{values['topic_prefix']}{values['title']}", 'msg': message})
        sleep_us(100)

def display_vals(display, data):
    start_x = 18,
    start_y = 16
    y_offset = 8
    for values in data:
        display.write_word(start_x, start_y, f"{values['title'].upper()}: {values['value']}")
        start_y += y_offset
    display.transmit()

#moisture sensor helper
def read_moisture(sensor):
    data = []
    for key in sensor.data_dimensions.keys():
        data.append({"value": sensor.tripped(key), "topic_prefix": 'plant1/{sensor.id}/', "title": key, "type": 'bool'})
    return data


#disable brownout trigger...I think
mem32[0x3ff48000+0xd4] = 0

#setup moisture sensor
moist = OnboardTouchPad(moisture)
moist.setup()

#set up sensors with I2C
i2c_bus = I2C(i2c.config)
ht_sensor = SHTC3(shtc3.config)
uv_sensor = SI1145(si1145.config)
reqs = {'i2c': i2c_bus}
ht_sensor.setup(reqs)
uv_sensor.setup(reqs)


#set up display with SPI
spi_bus = SPI(spi.config)
screen = SSD1327(ssd.config)
screen.setup({'spi': spi_bus})

#set up mqtt with Wifi
wifi = WLAN(wlan_config)
mosq = Mqtt(mqtt_config)
mosq.setup({'wlan': wifi})

#loop
while True:
    #read sensor values
    ht_sensor.receive()
    uv_sensor.receive()
    moist.receive()
    moisture_data = read_moisture(moist)
    #calculate relevant data from sensors
    temp = ht_sensor.temperature
    humid = ht_sensor.humidity
    dp = ht_sensor.dewpoint(temp, humid)
    uv = uv_sensor.uv_index
    lux = uv_sensor.lux
    ir = uv_sensor.infrared


    data = [
        {"value": uv, "topic_prefix": 'plant1/{uv_sensor.id}/' ,"title": 'uv_index', "type": 'float'},
        {"value": ir, "topic_prefix": 'plant1/{uv_sensor.id}/' ,"title": 'ir_irradiance', "type": 'float'},
        {"value": lux, "topic_prefix": 'plant1/{uv_sensor.id}/' ,"title": 'lux', "type": 'float'},
        {"value": humid, "topic_prefix": 'plant1/{ht_sensor.id}/' ,"title": 'humidity', "type": 'float'},
        {"value": temp, "topic_prefix": 'plant1/{ht_sensor.id}/' ,"title": 'temperature', "type": 'float'},
        {"value": dp, "topic_prefix": 'plant1/{ht_sensor.id}/' ,"title": 'dewpoint', "type": 'float'},
    ]
    data.extend(moisture_data)

    display_vals(screen, data)
    mqtt_masspub(mosq, data)    
