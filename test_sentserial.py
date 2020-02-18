import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
serialPort = serial.Serial(port='com10',baudrate=9600,parity=serial.PARITY_ODD,stopbits=serial.STOPBITS_TWO,bytesize=serial.SEVENBITS)

serialPort.isOpen()

while(1):
    # The b at the beginning is used to indicate bytes!
    serialPort.write(b"Thank you for sending data \r\n")