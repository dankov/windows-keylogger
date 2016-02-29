# Simple Windows Keylogger #
A dead simple keylogger for Windows in C which writes key up and key down events to stdout. Alongside is a collection of Python scripts to turn that output into something useful. Right now the scripts can easily generate a list of most commonly pressed keys and key combinations.

This is a keylogger because it logs keys, but it does not fit the connation of keylogger as malware. It does not have features for running automatically or covertly. It does not do anything remotely. It is designed to be run manually inside an open CMD window. You are encouraged to build it from source.

## Tools ##

### `keylogger.c` ###
Uses the Win32 API to listen to key presses. Emits up and down events for the virtual key codes of all keys in decimal.

#### stdout ####
```
up 13
down 160
down 160
down 72
up 72
up 160
down 69
up 69
down 76
up 76
down 76
down 79
down 188
up 188
up 76
up 79
down 32
down 160
down 87
up 87
up 160
down 79
up 79
up 32
down 82
up 82
down 76
up 76
down 68
up 68
down 160
down 49
up 49
up 160
down 162
down 160
down 37
up 37
down 37
up 37
down 37
up 37
down 37
up 37
up 160
up 162
down 46
up 46
down 162
down 67
```

#### stderr ####
```
Logging keys. Ctrl+C to exit.
```

### `combine_keys.py` ###
Converts a stream of key up and key down events into the pressed key combinations

#### stdin ####
```
up 13
down 160
down 160
down 72
up 72
up 160
down 69
up 69
down 76
up 76
down 76
down 79
down 188
up 188
up 76
up 79
down 32
down 160
down 87
up 87
up 160
down 79
up 79
up 32
down 82
up 82
down 76
up 76
down 68
up 68
down 160
down 49
up 49
up 160
down 162
down 160
down 37
up 37
down 37
up 37
down 37
up 37
down 37
up 37
up 160
up 162
down 46
up 46
down 162
down 67
```

#### stdout ####
```
160
160
160 72
69
76
76
76 79
76 79 188
32
32 160
32 160 87
32 79
82
76
68
160
160 49
162
162 160
162 160 37
162 160 37
162 160 37
162 160 37
46
162
162 67
```

#### stderr ####
```
Key 13 went up without going down on line 1
```

### `name_keys.py` ###
Converts numbered key combinations into named key combinations

#### stdin ####
```
160
160
160 72
69
76
76
76 79
76 79 188
32
32 160
32 160 87
32 79
82
76
68
160
160 49
162
162 160
162 160 37
162 160 37
162 160 37
162 160 37
46
162
162 67
```

#### stdout ####
```
LSHIFT
LSHIFT
LSHIFT h
e
l
l
l o
l o ,
SPACE
SPACE LSHIFT
SPACE LSHIFT w
SPACE o
r
l
d
LSHIFT
LSHIFT 1
LCTRL
LCTRL LSHIFT
LCTRL LSHIFT LEFT
LCTRL LSHIFT LEFT
LCTRL LSHIFT LEFT
LCTRL LSHIFT LEFT
DEL
LCTRL
LCTRL c
```

### `remove_pre_mod_presses.py` ###
Removes insignificant key presses before modifier keys. (ex, holding `a` and pressing `CTRL` is the same as just pressing `CTRL`)

#### stdin ####
```
LSHIFT
LSHIFT
LSHIFT h
e
l
l
l o
l o ,
SPACE
SPACE LSHIFT
SPACE LSHIFT w
SPACE o
r
l
d
LSHIFT
LSHIFT 1
LCTRL
LCTRL LSHIFT
LCTRL LSHIFT LEFT
LCTRL LSHIFT LEFT
LCTRL LSHIFT LEFT
LCTRL LSHIFT LEFT
DEL
LCTRL
LCTRL c
```

#### stdout ####
```
LSHIFT
LSHIFT
LSHIFT h
e
l
l
l o
l o ,
SPACE
LSHIFT
LSHIFT w
SPACE o
r
l
d
LSHIFT
LSHIFT 1
LCTRL
LCTRL LSHIFT
LCTRL LSHIFT LEFT
LCTRL LSHIFT LEFT
LCTRL LSHIFT LEFT
LCTRL LSHIFT LEFT
DEL
LCTRL
LCTRL c
```

### `remove_mod_presses.py` ###
Removes all key combinations which are just modifier keys. (ex, `LCTRL LSHIFT` is removed, but `LCTRL LSHIFT t` is kept) Note that this removes some significant presses like hitting 'WIN' to open the Start Menu.


#### stdin ####
```
LSHIFT
LSHIFT
LSHIFT h
e
l
l
l o
l o ,
SPACE
LSHIFT
LSHIFT w
SPACE o
r
l
d
LSHIFT
LSHIFT 1
LCTRL
LCTRL LSHIFT
LCTRL LSHIFT LEFT
LCTRL LSHIFT LEFT
LCTRL LSHIFT LEFT
LCTRL LSHIFT LEFT
DEL
LCTRL
LCTRL c
```

#### stdout ####
```
LSHIFT h
e
l
l
l o
l o ,
SPACE
LSHIFT w
SPACE o
r
l
d
LSHIFT 1
LCTRL LSHIFT LEFT
LCTRL LSHIFT LEFT
LCTRL LSHIFT LEFT
LCTRL LSHIFT LEFT
DEL
LCTRL c
```

### `split_presses.py` ###
Split up combinations of held non-modifier keys onto their own lines. (ex, `a` then `a b` is the same as `a` then `b`)


#### stdin ####
```
LSHIFT h
e
l
l
l o
l o ,
SPACE
LSHIFT w
SPACE o
r
l
d
LSHIFT 1
LCTRL LSHIFT LEFT
LCTRL LSHIFT LEFT
LCTRL LSHIFT LEFT
LCTRL LSHIFT LEFT
DEL
LCTRL c
```

#### stdout ####
```
LSHIFT h
e
l
l
o
,
SPACE
LSHIFT w
o
r
l
d
LSHIFT 1
LCTRL LSHIFT LEFT
LCTRL LSHIFT LEFT
LCTRL LSHIFT LEFT
LCTRL LSHIFT LEFT
DEL
LCTRL c
```

### `merge_left_right.py` ###
Renames left and right versions of modifier keys to be neutral. (ex, `LCTRL` becomes `CTRL`)

#### stdin ####
```
LSHIFT h
e
l
l
o
,
SPACE
LSHIFT w
o
r
l
d
LSHIFT 1
LCTRL LSHIFT LEFT
LCTRL LSHIFT LEFT
LCTRL LSHIFT LEFT
LCTRL LSHIFT LEFT
DEL
LCTRL c
```

#### stdout ####
```
SHIFT h
e
l
l
o
,
SPACE
SHIFT w
o
r
l
d
SHIFT 1
CTRL SHIFT LEFT
CTRL SHIFT LEFT
CTRL SHIFT LEFT
CTRL SHIFT LEFT
DEL
CTRL c
```

## Usage ###

### Setup ###
1. Download and install [Visual Studio Community](https://www.visualstudio.com/products/free-developer-offers-vs)
2. Download and install the [latest version of Python for Windows](https://www.python.org/downloads/windows/)
3. Download and install the [latest version of Git for Windows](https://github.com/git-for-windows/git/releases/latest)

### Build ###
1. Open Developer Command Prompt for VS2015
2. Run `cl /TC keylogger.c /link user32.lib`
3. You will now have keylogger.exe

### Run ###
1. Open CMD as administrator
2. Run `keylogger.exe >> output.tmp`
3. Press `Ctrl+C` to end the program

### Analyze ###
1. Open Git Bash
2. Run `cat output.tmp | python combine_keys.py | python name_keys.py | python remove_pre_mod_presses.py | python remove_mod_presses.py  | python split_presses.py | python merge_left_right.py | sort | uniq -c | sort -n -k 1`