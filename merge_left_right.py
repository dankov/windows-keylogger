from __future__ import print_function
import fileinput
import sys

key_merge_map = {
    'LSHIFT' : 'SHIFT',
    'RSHIFT' : 'SHIFT',
    'LCTRL' : 'CTRL',
    'RCTRL' : 'CTRL',
    'LWIN' : 'WIN',
    'RWIN' : 'WIN',
    'LALT' : 'ALT',
    'RALT' : 'ALT'
}

for line in fileinput.input():
    split_line = line.rstrip().split(' ')

    output = ''
    for key in split_line:
        if key in key_merge_map:
            output += key_merge_map[key] + ' '
        else:
            output += key + ' '

    print(output.rstrip())