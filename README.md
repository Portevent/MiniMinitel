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


# Setup
## Python
Library is written with Python 3.10, no support for other version are guaranteed (should be compatible Python 3.11+)
```commandline
pip install miniminitel
```

## Minitel
Minitel need to be pluggged to computer throught serial port.  
Minital has a short but dense history, multiple early formats and functionalities appeared and co-lived.
User must be aware that some features may look similar or duplicate, and this library intends to simply expose
the functions, not select one. Don't be afraid to try them all and understand the subtle changes.
MiniMinitel main class hierarchy is based on my own understanding of protocoles and layers of functionalities.
It may be inacurate and is certainly incomplete

Minitel supports several modes :
- Teletel Videotex mode : default when booting Minitel. Use 40 columns display  
- Teletel Mixte mode : can be prompted by the server. Use 80 columns display  
- Teleinformatique : Ascii mode, can be prompted by the server or user (Fnct + T then A). Use 80 columns display

## Docs
### MiniMinitel

Simple interface
- `_write_csi`
- `_videotex_to_mixte`
- `_mixte_to_videotex`
- `_teletel_to_teleinformatique`
- `_teleinformatique_to_videotex`
- `cursor_on`
- `cursor_off`
- `switch_to_g1` # Display images
- `revert_to_g0` # Revert to standard alphanum characters

Videotex support :
- `write`(text: str)
- `shift_cursor_down`()
- `shift_cursor_up`()
- `shift_cursor_left`()
- `shift_cursor_right`()
- `cariage_return`()
- `return_to_top_left`()
- `explicit_article_separator`()
- `complete_to_end_of_line`()
- `clear`()
- `ring_bel`()
- `ask_cursor_pos`() Note : script must listen to input to recieve the response

CSI
- `cursor_move_to`(x: int, y: int)
- `move_cursor_up`(n: int = 1)
- `move_cursor_down`(n: int = 1)
- `move_cursor_right`(n: int = 1)
- `move_cursor_left`(n: int = 1)

- `clear_screen`()
- `clear_all_after`()
- `clear_all_before`()
- `clear_row_end`()
- `clear_row_start`()
- `clear_row`()

- `insert_rows`(count: int)
- `clear_rows`(count: int)
- `clear_characters`(count: int)

- `insert_mode_on`()
- `insert_mode_off`()

Turn on and off Videotex attributes
- `set_grandeur_normale`() 
- `set_double_hauteur`() 
- `set_double_largeur`() 
- `set_double_grandeur`() 
- `set_blinking`() 
- `set_non_blinking`() 
- `set_inverted_color`() 
- `set_non_inverted_color`() 

Display image (or "buggy" alternative)
- `display_image`(filepath: str, mode="resize", bg_color=(0, 0, 0))
- `show_image_buggy`(filepath: str, mode="resize", bg_color=(0, 0, 0))  

Shortcut methods that revert to grandeur normale :
- `write_double_grandeur`()
- `write_double_largeur`()
- `write_double_hauteur`() 

## Input
Input are recieved as one object, either containing text or a code :

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
List of codes :
- TEXT 
- ENVOI
- SOMMAIRE
- ANNULATION
- RETOUR
- REPETITION
- GUIDE
- CORRECTION
- SUITE
- MOVE_UP
- MOVE_DOWN
- MOVE_RIGHT
- MOVE_LEFT
- GO_BACK_UP
- INSERT_LINE
- SUPPR_LINE
- SUPPR_COLUMN
- INSERT_COLUMN
- E_Page
- CONNEXION
- BS
- LF
- CAN
- TAB
- BRK
- DELETE
- CARRIAGE_RETURN
- UNKNOWN_CODE
