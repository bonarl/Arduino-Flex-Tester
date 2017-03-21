# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 13:38:46 2017

@author: bonar
"""
from Expander import EXPANDER
#flex-tools
#functions used in flex-tester code


p1PinList = ['SP6_1', 'SP6_1', 'SP6_1', 'SP6_1', 'SP6_1', 'DCS_BUS2', 'DCS_BUS1', 'TAB1-2', 'TAB1-1', 'SP1_2', 'SP1_2', 'SP1_2', 'SP1_2', 'SP1_2', 'HV_SHIELD', 'HV_RET', 'No Net', 'No Net', 'No Net', 'HV', 'HV', 'No Net', 'No Net', 'No Net', 'HV_RET', 'HV_SHIELD', 'SP1_2', 'SP1_2', 'SP1_2', 'SP1_2', 'SP1_2', 'TAB1-3', 'TAB1-4', 'DCS_BUS3', 'DCS_PWR', 'SP6_1', 'SP6_1', 'SP6_1', 'SP6_1', 'SP6_1']

p2PinList = ['SP1_2', 'SP1_2', 'SP1_2', 'SP1_2', 'SP1_2', 'DCS_BUS2', 'DCS_BUS1', 'TAB2-2', 'TAB2-1', 'SP2_3', 'SP2_3', 'SP2_3', 'SP2_3', 'SP2_3', 'HV_SHIELD', 'HV_RET', 'No Net', 'No Net', 'No Net', 'HV', 'HV', 'No Net', 'No Net', 'No Net', 'HV_RET', 'HV_SHIELD', 'SP2_3', 'SP2_3', 'SP2_3', 'SP2_3', 'SP2_3', 'TAB2-3', 'TAB2-4', 'DCS_BUS3', 'DCS_PWR', 'SP1_2', 'SP1_2', 'SP1_2', 'SP1_2', 'SP1_2']

p3PinList = ['SP2_3', 'SP2_3', 'SP2_3', 'SP2_3', 'SP2_3', 'DCS_BUS2', 'DCS_BUS1', 'TAB3-2', 'TAB3-1', 'SP3_4', 'SP3_4', 'SP3_4', 'SP3_4', 'SP3_4', 'HV_SHIELD', 'HV_RET', 'No Net', 'No Net', 'No Net', 'HV', 'HV', 'No Net', 'No Net', 'No Net', 'HV_RET', 'HV_SHIELD', 'SP3_4', 'SP3_4', 'SP3_4', 'SP3_4', 'SP3_4', 'TAB3-3', 'TAB3-4', 'DCS_BUS3', 'DCS_PWR', 'SP2_3', 'SP2_3', 'SP2_3', 'SP2_3', 'SP2_3']

p4PinList = ['SP3_4', 'SP3_4', 'SP3_4', 'SP3_4', 'SP3_4', 'DCS_BUS2', 'DCS_BUS1', 'TAB4-2', 'TAB4-1', 'EOS_GND', 'EOS_GND', 'EOS_GND', 'EOS_GND', 'EOS_GND', 'HV_SHIELD', 'HV_RET', 'No Net', 'No Net', 'No Net', 'HV', 'HV', 'No Net', 'No Net', 'No Net', 'HV_RET', 'HV_SHIELD', 'EOS_GND', 'EOS_GND', 'EOS_GND', 'EOS_GND', 'EOS_GND', 'TAB4-3', 'TAB4-4', 'DCS_BUS3', 'DCS_PWR', 'SP3_4', 'SP3_4', 'SP3_4', 'SP3_4', 'SP3_4']

p5PinList = ['EOS_SP', 'EOS_SP', 'EOS_SP', 'EOS_SP', 'EOS_SP', 'DCS_BUS2', 'DCS_BUS1', 'TAB5-2', 'TAB5-1', 'SP5_6', 'SP5_6', 'SP5_6', 'SP5_6', 'SP5_6', 'HV_SHIELD', 'HV_RET', 'No Net', 'No Net', 'No Net', 'HV', 'HV', 'No Net', 'No Net', 'No Net', 'HV_RET', 'HV_SHIELD', 'SP5_6', 'SP5_6', 'SP5_6', 'SP5_6', 'SP5_6', 'TAB5-3', 'TAB5-4', 'DCS_BUS3', 'DCS_PWR', 'EOS_SP', 'EOS_SP', 'EOS_SP', 'EOS_SP', 'EOS_SP']

p6PinList = ['SP5_6', 'SP5_6', 'SP5_6', 'SP5_6', 'SP5_6', 'DCS_BUS2', 'DCS_BUS1', 'TAB6-2', 'TAB6-1', 'SP6_1', 'SP6_1', 'SP6_1', 'SP6_1', 'SP6_1', 'HV_SHIELD', 'HV_RET', 'No Net', 'No Net', 'No Net', 'HV', 'HV', 'No Net', 'No Net', 'No Net', 'HV_RET', 'HV_SHIELD', 'SP6_1', 'SP6_1', 'SP6_1', 'SP6_1', 'SP6_1', 'TAB6-3', 'TAB6-4', 'DCS_BUS3', 'DCS_PWR', 'SP5_6', 'SP5_6', 'SP5_6', 'SP5_6', 'SP5_6']

EoSJ1PinList = ['TAB3-2', 'TAB3-1', 'DCS_PWR', 'DCS_BUS3', 'LV_SHIELD', 'LV_SHIELD', 'LV_SHIELD', 'LV_SHIELD', 'LV_SHIELD', 'LV_SHIELD', 'LV_SHIELD', 'LV_SHIELD', 'LV_SHIELD', 'LV_SHIELD', 'LV_SHIELD', 'LV_SHIELD', 'DCS_BUS2', 'DCS_BUS1', 'TAB4-4', 'TAB4-3', 'TAB4-2', 'TAB4-1', 'TAB5-4', 'TAB5-3', 'TAB5-2', 'TAB5-1', 'TAB6-4', 'TAB6-3', 'TAB6-2', 'TAB6-1', 'TAB1-4', 'TAB1-3', 'TAB1-2', 'TAB1-1', 'TAB2-4', 'TAB2-3', 'TAB2-2', 'TAB2-1', 'TAB3-4', 'TAB3-3']

EoSJ2PinList = ['EOS_GND', 'EOS_GND', 'EOS_GND', 'EOS_GND', 'EOS_GND', 'EOS_SP', 'EOS_SP', 'EOS_SP', 'EOS_SP', 'EOS_SP', 'No Net', 'No Net', 'No Net', 'No Net', 'No Net', 'No Net', 'DCS_PWR', 'DCS_BUS3', 'DCS_BUS2', 'DCS_BUS1', 'LV_SHIELD', 'LV_SHIELD', 'No Net', 'No Net', 'No Net', 'No Net', 'No Net', 'No Net', 'No Net', 'No Net', 'EOS_SP', 'EOS_SP', 'EOS_SP', 'EOS_SP', 'EOS_SP', 'EOS_GND', 'EOS_GND', 'EOS_GND', 'EOS_GND', 'EOS_GND']

EoSJ3PinList = ['DCS_PWR', 'DCS_BUS3', 'DCS_BUS2', 'DCS_BUS1', 'No Net', 'No Net', 'No Net', 'No Net', 'No Net', 'No Net', 'No Net', 'HV_SHIELD', 'HV_RET', 'No Net', 'No Net', 'No Net', 'No Net', 'No Net', 'No Net', 'HV', 'HV', 'No Net', 'No Net', 'No Net', 'No Net', 'No Net', 'No Net', 'HV_RET', 'HV_SHIELD', 'No Net', 'No Net', 'No Net', 'No Net', 'No Net', 'No Net', 'No Net', 'No Net', 'No Net', 'LV_SHIELD', 'LV_SHIELD']


network = [p1PinList, p2PinList, EoSJ3PinList, p3PinList, EoSJ1PinList, p4PinList, EoSJ2PinList, p5PinList, p6PinList]
board_names = ['P1', 'P2', 'EoSJ3', 'P3', 'EoSJ1', 'P4', 'EoSJ2', 'P5', 'P6']  

baudrate = 115200
GPIO_HIGH = 's'
GPIO_LOW = 'c'
GPIO_IN = 'i'
GPIO_OUT = 'o'

#baudrate must be 115200 to match Arduino firmware
#GPIO signals are declared (these are the signals which Arduinos are set up to receive)

#function for checking expected matches between a sender pin and receiver pin list
#function compares sender pin name and finds any matches in receiver list (exception
#for no net where no matches should ever be found) function then returns dictionary
#with keys as pin numbers (as on circuit diagram) and entries as 0 or 1 for whether
#match is expected or not
def check_expected(sender_pin, receiver_pin_list):  
    expected = {}
    if str(sender_pin) == 'No Net':
        for i in range(len(receiver_pin_list)):
            expected[i+1] = 0
    else:
        for i in range(len(receiver_pin_list)):
            if str(sender_pin) == str(receiver_pin_list[i]):
                expected[i+1] = 1
            else:
                expected[i+1] = 0
    return(expected)
    
    
#function for reading logic values of pins on a receiver board through Arduino
def check_real(board):
    pinList = []
    matchList = []
    for port in range (0, 6):
        raw_value = board.portRead(port)
        if (port == 2 or port == 5):
            int_value = int(raw_value.rstrip())&0x0F 
        else:
            int_value = int(raw_value.rstrip())
        bin_value = "{:08b}".format(int_value)   
        valueList = list(bin_value)
        valueList.reverse() 
        for item in valueList:          
            pinList.append(item)        #pinlist is list length 48 , items with index 20 to 23 are id 
    for i in range(len(pinList)-8):     #ordering pinlist and removing id bits
        if i > 19:
            matchList.append(int(pinList[i+4]))
        else:
            matchList.append(int(pinList[i]))
    orderedlist = {}
    for j in range(len(matchList)):
        orderedlist[j+1] = matchlist(j)
    return(orderedlist)
    
def check_self(flex_dict, sender, sender_pin):
    expected = flex_dict[sender][sender_pin][sender]['expected']
    real = flex_dict[sender][sender_pin][sender]['real']
    net_status = False
    if real == expected:
        net_status = not net_status
    return(net_status)
    

class FLEX_TAPE:
    def __init__(self, network, board_names):

        self.dict= {}
        self.network = network
        self.board_names = board_names
        #a dictionary is set up containing the connector board names, pin lists, receiver boards, and check status and results of receiver board for that sender/pin
        for sboard in range(len(network)):
            self.dict['%s' % (board_names[sboard])] = {}
            for pin in range(len(network[sboard])):
                self.dict['%s' %(board_names[sboard])]['%s' % (network[sboard][pin])] = {}
                for i in range(len(board_names)):
                    rboard = board_names[i]
                    sender_pin = network[sboard][pin]
                    receiver_pin_list = network[i]
                    self.dict['%s' %(board_names[sboard])]['%s' % (sender_pin)]['%s' %(rboard)] = {'errors': False, 'checked': False, 'expected': check_expected(sender_pin, receiver_pin_list ), 'real': []}
                               
    def parse(self, sender, receiver, com_ports, baudrate):
        sender_int = self.board_names.index(sender)
        receiver_int = self.board_names.index(receiver)
        sender_list = self.network[sender_int]
        brd1 = EXPANDER(str(com_ports[sender_int]), baudrate)
        brd2 = EXPANDER(str(com_ports[receiver_int]), baudrate)
        
        for pin in range(40):      
            sender_pin = sender_list[pin]
            check_status = self.dict[sender][sender_pin][receiver]['checked']
            #this loop checks if the sender pin network has previously been checked on the receiver (as saved in the dictionary)
            #if not it sets the pin high and checks the receiver, logging the network in dictionary and marking as checked
            if self.dict[sender][sender_pin][receiver]['checked'] == False:  
                brd1.setAllInputs()
                brd1.pinFunction(pin, GPIO_OUT)
                brd1.writePin(pin, GPIO_HIGH)
                self.dict[sender][sender_pin][sender]['real'] = check_real(brd1)
                brd2.setAllInputs()
                self.dict[sender][sender_pin][receiver]['real'] = check_real(brd2)
                if check_self(self.dict, sender, sender_pin) == True:       
                    check_status = not check_status
                    print(check_status)
                brd1.writePin(pin, GPIO_LOW)
                self.dict[sender][sender_pin][receiver]['checked'] = check_status
     
    def net_parse(self, sender, receiver, com_ports, baudrate, socket, ext_board):
        sender_int = self.board_names.index(sender)
        receiver_int = self.board_names.index(receiver)
        sender_list = self.network[sender_int]
        go = ('go').encode('utf-8')
        brd1 = EXPANDER(str(com_ports[sender_int]), baudrate)
        brd2 = EXPANDER(str(com_ports[receiver_int]), baudrate)
        
        for pin in range(40):
            
            sender_pin = sender_list[pin]
            check_status = self.dict[sender][sender_pin][receiver]['checked']
            #this loop checks if the sender pin network has previously been checked on the receiver (as saved in the dictionary)
            #if not it sets the pin high and checks the receiver, logging the network in dictionary and marking as checked
            if check_status == False:  
                socket.send(go)
                brd1.setAllInputs()
                brd1.pinFunction(pin, GPIO_OUT)
                brd1.writePin(pin, GPIO_HIGH)
                self.dict[sender][sender_pin][sender]['real'] = check_real(brd1)
                self.dict[sender][sender_pin][receiver]['real'] = check_real(brd2)
                if check_self(self.dict, sender, sender_pin) == True:       
                    check_status = not check_status
                    print(check_status)
                brd1.writePin(pin, GPIO_LOW)
                self.dict[sender][sender_pin][receiver]['checked'] = check_status
                socket_results = socket.recv(1024)
            else:
                socket,send(pas)
            #set dictionary entry to results after decoding json object
            self.dict[sender][sender_pin][ext_board]['checked'] = True
            #socket_results.decode('utf-8') 
            #decode json object, set dict ext_board entry 
                                
    def net(self):
            return(self.dict)

                
            
                
                
            


     
