from __future__ import print_function
import fileinput
import sys

mod_keys = ['SHIFT','CTRL','ALT','LWIN','RWIN','LSHIFT','RSHIFT','LCTRL','RCTRL','LALT','RALT']

for line in fileinput.input():
    split_line = line.rstrip().split(' ')
    keys_to_keep = []
    for key in split_line:
        if key in mod_keys:
            keys_to_keep = [k for k in keys_to_keep if k in mod_keys]
        keys_to_keep.append(key)

    output = ''
    for key in keys_to_keep:
        output += key + ' '
    
    print(output.rstrip())