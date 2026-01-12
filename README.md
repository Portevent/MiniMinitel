# MiniMinitel
![](https://img.shields.io/badge/Version-1.0.4-blue)
![](https://img.shields.io/badge/CI-none-red)

MiniMinitel is a simple Minitel interface in python. It has been created with the help of :
- http://543210.free.fr/TV/stum1b.pdf
- https://wiki-ima.plil.fr/mediawiki/images/b/b1/Minitel.pdf
- https://github.com/eserandour/Minitel1B_Hard

> MiniMinitel is now live on PyPi !

```python
from miniminitel import MiniMinitel

with MiniMinitel("COM4") as minitel:
    minitel.clear()
    
    minitel.cursor_move_to(4, 4)
    minitel.write_double_grandeur("Hello world")

    minitel.write_at(6, 6, "I'm a MiniMinitel")
    minitel.set_blinking()
    minitel.write_at(6, 7, "And I look cool")
    minitel.set_non_blinking()
```

Use `.start_listening` to handle input. This example script will listen for input and echo them.
Special key, such as ENVOI, RETOUR, ANNULATION will be logged in Python's terminal.

```python
from miniminitel import MiniMinitel, MinitelInput, MinitelCode

def echo(value: MinitelInput):
    if value.code == MinitelCode.TEXT:
        minitel.write(value.text)
    else:
        print("Key pressed : " + value.code)

with MiniMinitel() as minitel:
    minitel.clear()
    # Press Fnct + T then E to remove Minitel echo
    # (or else key pressed will be echoed twice, by the Minitel and by this script)
    minitel.start_listening(echo)
```

# Setup
## Python
Library is written with Python 3.10, no support for other version are guaranteed (should be compatible Python 3.11+)
```commandline
pip install miniminitel
```

## Minitel
Minitel need to be pluggged to computer throught serial port. Documentation need to be written 
