
import time
import serial
arduinoData = serial.Serial('com3', 115200)
time.sleep(1)
while True:
    while(arduinoData.in_waiting==0):
        pass
    dataPacket= arduinoData.readline()
    dataPacket = str(dataPacket,'utf-8')
    dataPacket = dataPacket.strip('\r\n')
    print(dataPacket)
    if dataPacket == '0':
        print('Adukpo')
    else:
        print('loser')
