def configure(keymap):
    keymap.replaceKey('CapsLock', 'Ctrl')
    
    keymap_global = keymap.defineWindowKeymap()
    keymap_global['C-p'] = 'Up'
    keymap_global['C-n'] = 'Down'
    keymap_global['C-b'] = 'Left'
    keymap_global['C-f'] = 'Right'
    keymap_global['C-a'] = 'Home'
    keymap_global['C-e'] = 'End'
    
    keymap_global['C-w'] = 'C-x'
    keymap_global['C-y'] = 'C-v'
    
    keymap_global['A-f'] = 'C-f'
    keymap_global['A-w'] = 'C-w'
