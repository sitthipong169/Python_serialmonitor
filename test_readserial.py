import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
serialPort = serial.Serial(port='com10',baudrate=9600,parity=serial.PARITY_ODD,stopbits=serial.STOPBITS_TWO,bytesize=serial.SEVENBITS)

serialPort.isOpen()

while(1):
    # Wait until there is data waiting in the serial buffer
    if(serialPort.in_waiting > 0):
        # Read data out of the buffer until a carraige return / new line is found
        serialString = serialPort.readline()
        # Print the contents of the serial data
        print(serialString.decode('Ascii'))
