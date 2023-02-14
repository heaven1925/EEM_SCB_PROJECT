
"""
Shows how to receive messages via polling.
"""

import can
import time
from can.bus import BusState


def receive_all():
    """Receives all messages and prints them to the console until Ctrl+C is pressed."""

    # this uses the default configuration (for example from environment variables, or a
    # config file) see https://python-can.readthedocs.io/en/stable/configuration.html
    with can.Bus(interface='socketcan',
                 channel='can0',
                 receive_own_messages=True) as bus:          

        # set to read-only, only supported on some interfaces
        try:
            bus.state = BusState.PASSIVE
        except NotImplementedError:
            pass

        try:
            while True:
                msg = bus.recv(1)
                if msg is not None:
                    print(msg.data)                             
                   
        except KeyboardInterrupt:
            pass  # exit normally


#if __name__ == "__main__":
while True:
    receive_all()
    sleep(1)
