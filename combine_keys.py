from __future__ import print_function
import fileinput
import sys

keys_down = []
i = 0
for line in fileinput.input():
    i += 1
    split_line = line.rstrip().split(' ')
    if len(split_line) != 2:
        print('Unrecognized format on line ' + str(i), file=sys.stderr)
        continue
      
    action = split_line[0]
    key = split_line[1]
    if action == 'down':
        if key in keys_down:
            keys_down = [k for k in keys_down if k != key]
        keys_down.append(key)
        output = ''
        for key in keys_down:
            output += key + ' '
        output = output.rstrip()
        print(output)
    elif action == 'up':
        if key in keys_down:
            keys_down = [k for k in keys_down if k != key]
        else:
            print('Key ' + key + ' went up without going down on line ' + str(i), file=sys.stderr)
    else:
        print('Unrecognized input on line ' + str(i), file=sys.stderr)