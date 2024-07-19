from config.interface import I2C as i2c
from config.interface import SPI as spi

from config.pixel.monochrome import SSD1327 as ssd
from config.environment.moist import SHTC3 as shtc3
from config.environment.light import SI1145 as si1145
from config.application.remote.Mqtt import config as mqtt_config
from config.interface.comms.WLAN import config as wlan_config

from firmware.interface.I2C import I2C
from firmware.interface.SPI import SPI
from firmware.interface.comms.WLAN import WLAN
from firmware.application.remote.Mqtt import Mqtt
from firmware.pixel.monochrome.SSD1327 import SSD1327
from firmware.environment.moist.SHTC3 import SHTC3
from firmware.environment.light.SI1145 import SI1145

from json import dumps
from machine import deepsleep

#setup    
bus = I2C(i2c.config)
ht_sensor = SHTC3(shtc3.config)
uv_sensor = SI1145(si1145.config)

#spi_bus = SPI(spi.config)
#screen = SSD1327(ssd.config)
#screen.setup({'spi': spi_bus})

reqs = {'i2c': bus}
ht_sensor.setup(reqs)
uv_sensor.setup(reqs)

wifi = WLAN(wlan_config)

mosq = Mqtt(mqtt_config)

mosq.setup({'wlan': wifi})


mosq.main(hook='publish', publish_args={'topic': 'plant1/sensor1/temperature', 'msg': dumps({'data': 4})})
while True:
    temp = ht_sensor.temperature
    humid = ht_sensor.humidity
    dp = ht_sensor.dewpoint(temp, humid)

    mosq.main(hook='publish', publish_args={'topic': f'ficus/{uv_sensor.id}/uv_index', 'msg': bytes(uv_sensor.uv_index)})
    mosq.main(hook='publish', publish_args={'topic': f'ficus/{uv_sensor.id}/ir_irradiance', 'msg': bytes(uv_sensor.ir_irradiance)})
    mosq.main(hook='publish', publish_args={'topic': f'ficus/{uv_sensor.id}/lux', 'msg': bytes(uv_sensor.visible_lux)})

    mosq.main(hook='publish', publish_args={'topic': f'ficus/{ht_sensor.id}/humidity', 'msg': bytes(humid)})
    mosq.main(hook='publish', publish_args={'topic': f'ficus/{ht_sensor.id}/temperature', 'msg': bytes(temp)})
    mosq.main(hook='publish', publish_args={'topic': f'ficus/{ht_sensor.id}/dewpoint', 'msg': bytes(dp)})
    deepsleep(60000)

# 

# import machine
# import usocket as socket

# right = machine.Pin(0, machine.Pin.OUT)
# rightpwm = machine.PWM(right)
# 
# rightpwm.freq(100)
# 
# rightpwm.duty_u16(65535)
# 
# left = machine.Pin(1, machine.Pin.OUT)
# leftpwm = machine.PWM(left)
# 
# leftpwm.freq(100)
# 
# leftpwm.duty_u16(65535)


# 
# 
# 
# #print(ht_sensor.current_data)
# while 1:
#     ht_sensor.receive()
#     uv_sensor.receive()
#     irr = uv_sensor.ir_irradiance()
#     lux = uv_sensor.indoor_visible_lux()
#     print(irr, lux)
#     #screen.set_pixel(64, 64, 0xF)
#     screen.write_word(24, 32, f"ir rad: {irr}".upper())
#     screen.write_word(24, 40, f"vis lux: {lux}".upper())
#     screen.write_word(24, 48, f"ir rad: {irr}".upper())
#     screen.write_word(24, 56, f"vis lux: {lux}".upper())
# #screen.load_bmp(0, 0, "test.bmp")
#     
#     screen.transmit()


