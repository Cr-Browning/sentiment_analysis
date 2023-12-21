# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 19:47:28 2023

@author: Cade Browning

Takes the special values on the keyboard such as Space, Control, and Backspace,
    and makes them more legible in the txt file of the keylogger rather than Key.Backspace, etc
"""

def KeyInput(value):
    """
    Parameters
    ----------
    value : TYPE str
        value is the key input from the keyboard
    Returns
    -------
    TYPE str
        retuns a clearer depiction of they key that was pressed, this function only impacts special keys such as
            Space, Control, and Backspace.
    """
    value = str(value)
    value = value.replace("'", "")
    
    if value =='Key.space':
        value = '\n'
    
    if value =='Key.shift':
        value = value.upper()
        
    if value =='Key.alt':
        value = ''
        
    if value =='Key.alt_gr':
        value = ''
        
    if value =='Key.alt_l':
        value = ''
        
    if value =='Key.alt_r':
        value = ''
        
    if value =='Key.backspace':
        value = value.replace('Key.backspace', '')
        value = value[:-1]
    
    if value =='Key.caps_lock':
        value = ''
    
    if value =='Key.cmd':
        value = ''
        
    if value =='Key.cmd_l':
        value = ''
        
    if value =='Key.cmd_r':
        value = ''
        
    if value =='Key.ctrl_l':
        value = ''
    
    if value =='Key.ctrl_r':
        value = ''
    
    if value =='Key.delete':
        value = ''
        
    if value =='Key.down':
        value = ''
    
    if value =='Key.up':
        value = ''
        
    if value =='Key.left':
        value = ''
        
    if value =='Key.right':
        value = ''
    
    if value =='Key.end':
        value = ''
        
    if value =='Key.enter':
        value = '\n'
        
    if value =='Key.esc':
        value = ''
        
    if value =='Key.home':
        value = ''
        
    if value =='Key.insert':
        value = ''
    
    if value =='Key.menu':
        value = ''
    
    if value =='Key.num_lock':
        value = ''
        
    if value =='Key.page_down':
        value = ''
        
    if value =='Key.page_up':
        value = ''
    
    if value =='Key.pause':
        value = ''
        
    if value =='Key.print_screen':
        value = ''
        
    if value =='Key.scroll_lock':
        value = ''
        
    if value =='Key.left':
        value = ''
        
    if value =='Key.tab':
        value = '     '
    return str(value)

           