# MiniMinitel
MiniMinitel is a simple Minitel interface in python. It has been created with the help of :
- http://543210.free.fr/TV/stum1b.pdf
- https://wiki-ima.plil.fr/mediawiki/images/b/b1/Minitel.pdf
- https://github.com/eserandour/Minitel1B_Hard

> MiniMinitel is a work in progress, no version are published to PyPI yet

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

# Setup
## Python
MiniMinitel is a work in progress, no version are published to PyPI yet.  
Library is written with Python 3.10, no support for other version are guaranteed (should be compatible Python 3.11+)
```commandline
pip install miniminitel
```

## Minitel
Minitel need to be pluggged to computer throught serial port. Documentation need to be written 
