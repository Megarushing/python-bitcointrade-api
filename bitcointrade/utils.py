from .errors import ArgumentError
from hashlib import sha256
digits58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def to_bytes(n, length, endianess='big'):
    h = '%x' % n
    s = ('0'*(len(h) % 2) + h).zfill(length*2).decode('hex')
    return s if endianess == 'big' else s[::-1]

def decode_base58(bc, length):
    n = 0
    for char in bc:
        n = n * 58 + digits58.index(char)
    return to_bytes(n,length, 'big')

def check_btc_address(address):
    try:
        bcbytes = decode_base58(address, 25)
        return bcbytes[-4:] == sha256(sha256(bcbytes[:-4]).digest()).digest()[:4]
    except Exception:
        return False

def check_values(value, arg, arg_value):
    if type(value) == type:
        if type(arg_value) != value:
            raise ArgumentError(u"Type of argument {} is invalid. It should be {}".format(arg, value))
    elif arg_value not in value:
        raise ArgumentError(u"Value of argument {} is invalid. It should be one of {}".format(arg, value))

def check_args(kwargs, required_parameters={}, optional_parameters={}):
    args = kwargs.keys()
    required_args = required_parameters.keys()
    optional_args = optional_parameters.keys()

    missing_args = list(set(required_args) - set(args))
    if len(missing_args) > 0:
        raise ArgumentError(u"Parameter {} is required".format(missing_args))

    for arg_name, arg_value in kwargs.items():
        if arg_name in optional_args:
            optional_value = optional_parameters[arg_name]
            check_values(optional_value, arg_name, arg_value)
        elif arg_name in required_args:
            required_value = required_parameters[arg_name]
            check_values(required_value, arg_name, arg_value)
