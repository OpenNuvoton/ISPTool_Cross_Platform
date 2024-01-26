import os
import sys
#import glob
import serial
import serial.tools.list_ports

def serial_ports():
    result = []
    ports = serial.tools.list_ports.comports()
    for p in ports:
        result.append(p.device)
    return result


if __name__ == '__main__':
    print(serial_ports())