import serial

class Serialm:
    def __init__(self, port, baudrate, parity, stopbits, bytesize):
        self.port = port
        self.baudrate = baudrate
        self.parity = parity
        self.stopbits = stopbits
        self.bytesize = bytesize
