import sys
import numpy as np
import time
import serial
import os

class arduino_flowreader():
    def __init__(self, parent, port_name, baud):
        self.parent = parent
        self._initialize_serial(baud, port_name)

    def _initialize_serial(self, baud, port_name):
        print(port_name)
        self.port_name = port_name
        self.ser = serial.Serial(self.port_name, baud, timeout=1)
        self.ser.reset_input_buffer()

    def query(self):
        v = self._get_from_arduino()
        self._ask_arduino()
        return v

    def _get_from_arduino(self):
        if self.ser.in_waiting > 0:
            try:
                msg = (5 * float(self.ser.readline().decode('utf-8').rstrip()))/1024 #5/1024 converts it to 5 V scale
                return msg
            except:
                return 0

    def _ask_arduino(self):
        #Make sure nothing is in buffer, otherwise something has gone wrong... arduino should have cleared buffer every time
        if (self.ser.in_waiting == 0):
            self.ser.write(b'h') #it shouldnt actually matter what you write to serial, as long as you write something
    