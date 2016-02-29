from __future__ import print_function
import fileinput
import sys

mod_keys = ['SHIFT','CTRL','ALT','LWIN','RWIN','LSHIFT','RSHIFT','LCTRL','RCTRL','LALT','RALT']

for line in fileinput.input():
    split_line = line.rstrip().split(' ')
    last_key = split_line[len(split_line)-1]
    if last_key not in mod_keys:
        print(line.rstrip())