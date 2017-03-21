import serial
import time

class EXPANDER():
    def __init__(self, port= "COM1", baudrate = 115200):
        self.ser = serial.Serial(port, baudrate, timeout=None)
        self.ser.flush()
      
    def setFunction(self, channel, value): #2 Expander chips have pins 0-47
        if not value in ['i', 'o']:
            raise ValueError("Requested function not supported")
        command = value + str(channel)
        self.ser.write(command.encode('ascii'))
        self.ser.readline()

    def pinFunction(self, boardPin, value): #Connector Board has pins 0-39
        if not value in ['i', 'o']:
            raise ValueError("Requested value not supported")        
        channel = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]
        self.setFunction(channel[boardPin], value)

    def setAllInputs(self): #Setting all pins to inputs
        command = 'I'
        self.ser.write(command.encode('ascii'))       
        self.ser.readline()

    def setAllOutputs(self): #Setting all pins to inputs
        command = 'O'
        self.ser.write(command.encode('ascii'))     
        self.ser.readline()

    def clearAllPins(self): #Clearing all pin Registers
        command = 'C'
        self.ser.write(command.encode('ascii'))     
        self.ser.readline()
        
    def portRead(self, bank): # BANK# 0 to 5 
        bankNo = [0, 1, 2, 24, 25, 26]     
        command = 'R' + str(bankNo[bank])
        self.ser.write(command.encode('ascii'))
        value = self.ser.readline()
        return value

    def digitalRead(self, channel): #2 Expander chips have pins 0-47
        self.ser.readline()#clear input buffer.
        command = 'r' + str(channel)
        self.ser.write(command.encode('ascii'))
        rv = str(self.ser.readline()) #Read line from serial port and convert to string
        if not rv[10] in ['0', '1']:
            raise ValueError("Requested value not supported")
        else:
            if rv[10] == '1':
                return True
            elif rv[10] == '0':
                return False
    
    def digitalWrite(self, channel, value): #2 Expander chips have pins 0-47
        if not value in ['c', 's']:
            raise ValueError("Requested value not supported")
        command = str(value) + str(channel)
        self.ser.write(command.encode('ascii'))
        self.ser.readline() 
    
    def writePin(self, boardPin, value): # Connector Board has pins 0-39
        if not value in ['c', 's']:
            raise ValueError("Requested value not supported")        
        channel = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]
        self.digitalWrite(channel[boardPin], value)

    def getBoardID(self):
        intValueList = []
        for port in range (0, 6):
            rawValue = self.portRead(port)
            intValue = int(rawValue.rstrip())
            intValueList.append(intValue)
        return ((intValueList[5]&0xF0) + ((intValueList[2]&0xF0)>>4))
