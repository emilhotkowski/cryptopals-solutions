import base64
from binascii import unhexlify

def hex_str_to_base64(s):
    byte_seq = unhexlify(s)
    #print(byte_seq)
    return base64.b64encode(byte_seq)

print(hex_str_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))