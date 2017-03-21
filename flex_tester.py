# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 11:44:17 2017

@author: bonar
"""

from port_finder import listSerialPorts
from Expander import EXPANDER

import serial
import time
import datetime
import socket 
import sys
from flex_tools import *
#Flex-Tape network
#all pins on all boards are named according to the network they belong to

com_ports = listSerialPorts().reverse()

#here an instance of flex_tape class is called and a a dictionary is created for storing test 
#results for sender/receiver board pairs, the dictionary is an attribute of the FLEX_TAPE
#instance and contains test results
#the dictionary is stuctured as flex_tape['sender name']['netname']['receiver name'] 
#the above key then contains the expected results reading the 'receiver' board when setting a pin with 
#that 'netname' high on the sender board. The expected results are a list [0, 1, 0, 1, ....] etc 
#describing the high or low logic of pins expected on the receiver, generated by comparing the
#sender and receiver pin lists and searching for common names. The real list is in the same format
#and shows the actual values read from each board, these lists are compared to find possible defects.

flex_tape = FLEX_TAPE(network, board_names)

#baudrate must be 115200 to match Arduino firmware
#GPIO signals are declared (these are the signals which Arduinos are set up to receive)
baudrate = 115200
GPIO_HIGH = 's'
GPIO_LOW = 'c'
GPIO_IN = 'i'
GPIO_OUT = 'o'

#this loop goes through every sender/receiver pair and parses the boards.
#results of each senderboard+senderpin+receiver board test are stored in FLEX_TAPE dictionary/net flex_tape.net()
for i in range(len(board_names)):
    sender = board_names[i]
    for j in range(i+1, len(board_names)-1):
        receiver = board_names[j]
        flex_tape.parse(sender, receiver, com_ports, baudrate)

results = flex_tape.net()

#then can check results for errors (if checked == true and errors == true) and display information



