import base64
import struct

def decode_bytearray(encoded_payload):
    byte_array = base64.b64decode(encoded_payload)
    value = struct.unpack('f', byte_array)[0]
    return value

encoded_payload = data.get('payload')
decoded_value = decode_bytearray(encoded_payload)
hass.states.set(data.get('entity_id'), decoded_value)