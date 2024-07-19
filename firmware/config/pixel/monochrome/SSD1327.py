import machine

config = {
    "hw_path":"",
    "hw_version":"1.0.0",
    "mhodule":"",
    "fw_version":"1.0.0",
    "date_code":"",
    "serial_number":"",
    "data":{
        "brightness":128 * 128 // 2
    },
    "firmware":{
        "id":"pixel",
        "batches":2,
        "fw_requirements":{},
        "pins":{
            "digital":{
                "reset":{"id":34, "mode":machine.Pin.OUT},
                "command":{"id":35, "mode":machine.Pin.OUT},
                # "write_clock":{"id":14, "mode":machine.Pin.OUT},
                # "read_clock":{"id":15, "mode":machine.Pin.OUT},
                # "d0":{"id":0, "mode":machine.Pin.OUT},
                # "d1":{"id":1, "mode":machine.Pin.OUT},
                # "d2":{"id":2, "mode":machine.Pin.OUT},
                # "d3":{"id":3, "mode":machine.Pin.OUT},
                # "d4":{"id":4, "mode":machine.Pin.OUT},
                # "d5":{"id":5, "mode":machine.Pin.OUT},
                # "d6":{"id":6, "mode":machine.Pin.OUT},
                # "d7":{"id":7, "mode":machine.Pin.OUT}
            },
            "analog":{}
        },
        "custom_params":""
    },
    "elec":{
        "voltage":["3.3V", "15V"],
        "current":["0.1A", "0.1A"],
        "layout":{"x":10, "y":10, "path":""}
    }
}