# GTW: Green Thumb Wireless (_not a phone company_)
Collect metrics from plant over MQTT and store for monitoring in 
## Requirements:
### HomeAssistant
- Docker
### MicroController
- [Thonny](https://thonny.org/)

## Setup
### HomeAssistant
HomeAssistant, the MQTT broker and the other dependencies can be started with `docker compose up -d`
### Firmware
 - Install Micropython
 - Configure the files in `config/`
    - `config/application/remote/MQTT.py`: set the IP address/domain name of the MQTT broker
    - `config/interface/comms/WLAN.py`: set SSID & Password for to connect to WIFI
 - Install everything in top level firmware directory onto the microcontroller

