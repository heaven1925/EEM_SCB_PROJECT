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
