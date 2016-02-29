from __future__ import print_function
import fileinput
import sys

mod_keys = ['SHIFT','CTRL','ALT','LWIN','RWIN','LSHIFT','RSHIFT','LCTRL','RCTRL','LALT','RALT']

for line in fileinput.input():
    split_line = line.rstrip().split(' ')
    split_line_len = len(split_line)
    if split_line_len < 2:
        print(line.rstrip())
        continue

    last_key = split_line[len(split_line)-1]
    next_to_last_key = split_line[len(split_line)-2]
    if last_key in mod_keys or next_to_last_key in mod_keys:
        print(line.rstrip())
        continue

    mod_keys_pressed = [k for k in split_line if k in mod_keys]
    output = ''
    for key in mod_keys_pressed:
        output += key + ' '
    output += last_key
    print(output)