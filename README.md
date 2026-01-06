# MiniMinitel
MiniMinitel is a simple Minitel interface in python. It has been created with the help of :
- http://543210.free.fr/TV/stum1b.pdf
- https://wiki-ima.plil.fr/mediawiki/images/b/b1/Minitel.pdf
- https://github.com/eserandour/Minitel1B_Hard

> MiniMinitel is a work in progress, no version are published to PyPI yet

```python
from minitel import DOUBLE_GRANDEUR, CLIGNOTEMENT, MAJENTA, BLANC, GRANDEUR_NORMALE, MinitelController
# with MinitelController(port, baudrate)
with MinitelController("COM4") as minitel:
    minitel.returnToTopLeftAndClearScreen()
    minitel.cursorMoveTo(4, 4)

    minitel._setAttribute(DOUBLE_GRANDEUR)
    minitel._setAttribute(MAJENTA)
    minitel.write("Example")
    minitel._setAttribute(BLANC)
    minitel.write(" text")

    minitel.cursorMoveTo(6, 6)
    minitel._setAttribute(GRANDEUR_NORMALE)
    minitel._setAttribute(CLIGNOTEMENT)
    minitel.write("Hello world")
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
