"""
EEM_SCB_PROJECT
@a.ertekin
13.02.2023

This is a state machine implementation in Python, where the states
are defined as enumerations (enum.Enum). There are several states
and state-machines defined in this code:

MAIN_STATE: Defines the main state of the system (IDLE, ROUTINE, PROCESS, SUSPEND, DEINIT).
PROCESS_STATE: Defines the state of the process (IDLE, CAN, CAMERA, SDCARD, SUSPEND).
CAN_STATE: Defines the state of the CANBUS process (IDLE, ROUTINE, RECEIVE, TRANSMIT, SUSPEND).
CAMERA_STATE: Defines the state of the camera process (IDLE, ROUTINE, START, STOP, SUSPEND).
SDCARD_STATE: Defines the state of the SD-card process (IDLE, ROUTINE, SAVE, ERASE, SUSPEND).
There is also a class called 'stateMachine' that holds the instances of these
states and implements methods to change the states. The state-machines are executed
in the 'MAIN_State', 'PROCESS_STATE', 'CAN_STATE', 'CAMERA_STATE', and 'SDCARD_STATE' methods.
These methods contain logic to perform operations based on the current state.
"""

###################### import part #########################
import time
import enum
import time
import serial
import string

import can

###################### state machine part #################

class MAIN_STATE(enum.Enum):
    IDLE    = 0
    ROUTINE = 1
    PROCESS = 2
    SUSPEND = 3
    DEINIT  = 4

class PROCESS_STATE(enum.Enum):
    IDLE    = 0
    CAN     = 1
    CAMERA  = 2
    SDCARD  = 3
    SUSPEND = 4

class CAN_STATE(enum.Enum):
    IDLE     = 0
    ROUTINE  = 1
    RECEIVE  = 2
    TRANSMIT = 3
    SUSPEND = 4

class CAMERA_STATE(enum.Enum):
    IDLE = 0
    ROUTINE = 1
    START   = 2
    STOP    = 3
    SUSPEND = 4

class SDCARD_STATE(enum.Enum):
    IDLE = 0
    ROUTINE = 1
    SAVE    = 2
    ERASE   = 3
    SUSPEND = 4

class stateMachine:
    def __init__(self):
        self.mainState          = MAIN_STATE.IDLE;
        self.processState       = PROCESS_STATE.IDLE
        self.canProcessState    = CAN_STATE.IDLE
        self.cameraProcessState = CAMERA_STATE.IDLE
        self.sdCardProcessState = SDCARD_STATE.IDLE
        
    def runStateMachine(self):
        while True:
            self.MAIN_State()
    # State-Switch Methods #
    def setMainState(self, mainState):
        self.mainState = mainState ;
    def setProcessState(self, processState ):
        self.processState = processState
    def setCanState(self, canState):
        self.canProcessState = canState
    def setCameraState(self, cameraState):
        self.cameraProcessState = cameraState
    def setSDCardState(self, sdCardState):
        self.sdCardProcessState = sdCardState
    ################### Main-State Methods ##################
    def MAIN_State(self):
        if self.mainState is MAIN_STATE.IDLE:
            ######### MAIN ROUTINE OPERATIONS ########
            print("MAIN STATE - IDLE \n")
            """
            IDLE Methods etc.
            """
            self.setMainState(MAIN_STATE.ROUTINE)
            ##########################################
        elif self.mainState is MAIN_STATE.ROUTINE:
            ######### MAIN ROUTINE OPERATIONS ########
            print("MAIN STATE - ROUTINE \n")
            sendMessage(123,[1,2,3,4,5,6,7,8])
            """
            Routine Methods etc.
            """
            ##########################################
        elif self.mainState is MAIN_STATE.PROCESS:
            ######### MAIN PROCESS OPERATIONS ########
            """
            Process Methods etc.
            """
            ##########################################
        elif self.mainState is MAIN_STATE.SUSPEND:
            ######### MAIN PROCESS OPERATIONS ########
            self.setMainState(MAIN_STATE.IDLE)
            ##########################################
        else:
            self.setMainState(MAIN_STATE.SUSPEND)
    ###########################################################
    ################### Process-State Methods #################
    def PROCESS_STATE(self):
        if self.processState is PROCESS_STATE.IDLE:
            ######### PROCESS IDLE OPERATIONS ########
            """
            IDLE Methods etc.
            """
            self.setProcessState(PROCESS_STATE.ROUTINE)
            ##########################################
        elif self.processState is MAIN_STATE.ROUTINE:
            ######### PROCESS ROUTINE OPERATIONS ########                 
            """
            Routine Methods etc.
            """
            ##########################################
        elif self.processState is PROCESS_STATE.CAN:
            ######### PROCESS CAN OPERATIONS ########
            """
            CANBUS State-Machine Methods etc.
            """
            ##########################################
        elif self.processState is PROCESS_STATE.CAMERA:
            ######### PROCESS CAMERA OPERATIONS ######
            """
            CAMERA State-Machine Methods etc.
            """
            ##########################################
        elif self.processState is PROCESS_STATE.SDCARD:
            ######### PROCESS SDCARD OPERATIONS ######
            """
            SDCARD State-Machine Methods etc.
            """
            ##########################################
        elif self.processState is PROCESS_STATE.SUSPEND:
            self.setProcessState(PROCESS_STATE.IDLE)
        else:
            self.setProcessState(MAIN_STATE.SUSPEND)

    ###########################################################
    def CAN_STATE(self , msg):
        if self.canProcessState is CAN_STATE.IDLE:
            ######### CAN IDLE OPERATIONS ########
            """
            CAN IDLE Methods etc.
            """
            self.setCanState(CAN_STATE.ROUTINE)
            ##########################################
        elif self.canProcessState is CAN_STATE.ROUTINE:
            ######### CAN ROUTINE OPERATIONS ########
            """
            CAN ROUTINE Methods etc.
            """
            ##########################################
        elif self.canProcessState is CAN_STATE.TRANSMIT:
            ######### CAN TRANSMIT OPERATIONS ########
            """
            CAN Transmit Methods etc.
            """
            #########################################
        elif self.canProcessState is CAN_STATE.RECEIVE:
            ######### CAN RECEIVE OPERATIONS ########
            """
            CAN Receive Methods etc.
            """
            #########################################
        elif self.canProcessState is CAN_STATE.SUSPEND:
            self.setCanState(CAN_STATE.IDLE)
        else:
            self.setCanState(CAN_STATE.SUSPEND)
    ############## Camera-State Methods #######################
        if self.cameraProcessState is CAMERA_STATE.IDLE:
            ######### CAN IDLE OPERATIONS ########
            """
            CAMERA IDLE Methods etc.
            """
            self.setCameraState(CAMERA_STATE.ROUTINE)
            ##########################################
        elif self.cameraProcessState is CAMERA_STATE.ROUTINE:
            ######### CAN ROUTINE OPERATIONS ########
            """
            CAMERA ROUTINE Methods etc.
            """
            ##########################################
        elif self.cameraProcessState is CAMERA_STATE.START:
            ######### CAN TRANSMIT OPERATIONS ########
            """
            CAMERA START Methods etc.
            """
            #########################################
        elif self.cameraProcessState is CAMERA_STATE.STOP:
            ######### CAN RECEIVE OPERATIONS ########
            """
            CAMERA STOP Methods etc.
            """
            #########################################
        elif self.cameraProcessState is CAMERA_STATE.SUSPEND:
            self.setCameraState(CAMERA_STATE.IDLE)
        else:
            self.setCameraState(CAMERA_STATE.SUSPEND)
    ###########################################################
    ############## SDCard-State Methods #######################
        if self.sdCardProcessState is SDCARD_STATE.IDLE:
             ######### CAN IDLE OPERATIONS ########
            """
            CAMERA IDLE Methods etc.
            """
            self.setSDCardState(SDCARD_STATE.ROUTINE)
            ##########################################
        elif self.sdCardProcessState is SDCARD_STATE.ROUTINE:
            ######### CAN ROUTINE OPERATIONS ########
            """
            CAMERA ROUTINE Methods etc.
            """
            ##########################################
        elif self.sdCardProcessState is SDCARD_STATE.SAVE:
            ######### CAN TRANSMIT OPERATIONS ########
            """
            CAMERA START Methods etc.
            """
            #########################################
        elif self.sdCardProcessState is SDCARD_STATE.ERASE:
            ######### CAN RECEIVE OPERATIONS ########
            """
            CAMERA STOP Methods etc.
            """
            #########################################
        elif self.sdCardProcessState is SDCARD_STATE.SUSPEND:
            self.setSDCardState(SDCARD_STATE.IDLE)
        else:
            self.setSDCardState(SDCARD_STATE.SUSPEND)
        ###########################################################

###########################################################
 
##################### function definition #################
from can.bus import BusState

def recvMessage():
    """Receives all messages and prints them to the console until Ctrl+C is pressed."""

    # this uses the default configuration (for example from environment variables, or a
    # config file) see https://python-can.readthedocs.io/en/stable/configuration.html
    with can.Bus(interface='socketcan',
                 channel='can0',
                 receive_own_messages=True) as bus:          

        try:
            bus.state = BusState.PASSIVE
        except NotImplementedError:
            pass

        try:
            msg = bus.recv(1)
            return msg
        except KeyboardInterrupt:
            return 0  # exit normally

def sendMessage(id,msg):
    
    with can.Bus(interface='socketcan',
                 channel='can0',
                 receive_own_messages=True) as bus:
        
        message = can.Message(
            arbitration_id=id , data=msg, is_extended_id=True
            )
        
        try:
            bus.send(message)
            return 1
        except can.CanError:
            return 0

###################### init part ###########################      

machine = stateMachine()
machine.runStateMachine()

while True:
    msg = recvMessage()
    print(msg)
    sendMessage(123,[1,2,3,4,5,6,7,8])
    
# 
# ###################### main while part ######################
# 
# 


