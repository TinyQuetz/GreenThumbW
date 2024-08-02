from machine import Pin
config = {
    "hw_path":"",
    "hw_version":"",
    "module":"",
    "fw_version":"",
    "date_code":"",
    "serial_number":"",
    "data":{
        "moisture_1": 2,
        "moisture_2": 2
    },
    "firmware":{
        "id":"moist_sensor",
        "fw_requirements":{

        },
        "pins":{
            "digital":{ #key-value of pins
                "moisture_1":{"id":12, "mode":Pin.IN},
                "moisture_2": {"id":14, "mode": Pin.IN}}
        },
        "threshold": 40,
        "inverted": False
    }
}