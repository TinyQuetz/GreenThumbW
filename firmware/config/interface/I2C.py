from machine import Pin
config = {
    "hw_path":"",
    "hw_version":"",
    "mhodule":"",
    "fw_version":"",
    "date_code":"",
    "serial_number":"",
    "data":{
    },
    "firmware":{
        "id":"ic2_1",
        "fw_requirements":{},
        "pins":{
            "digital":{
                "scl":{"id":17, "mode":Pin.OUT}, 
                "sda": {"id":16, "mode": Pin.OUT}
            },
            "analog":{}
        },
        "channel": 0,
        "freq": 100000
    },
    "elec":{}
}