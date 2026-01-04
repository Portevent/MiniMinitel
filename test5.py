import serial

from minitel.minitel import Minitel

def get_word(ser: serial.Serial):
    return ser.read() + ser.read()


def print_form(_min: Minitel, f_u: str, f_p: str):
    _min.writeAt(5, 5, "Username: "+ f_u + max(25-len(f_u), 0)*'_')
    _min.writeAt(5, 6, "Password: " + min(25, len(f_p)) * "*")

def check_and_print(_min: Minitel, username: str, password: str):
    if username == "STAR-L0704" and password == "FKLRLOVR":
        s = "Authentication successful!"
    else:
        s = "Authentication failed!"

    print(s)
    _min.writeAt(30, 30-len(s)//2, s)


with Minitel() as minitel:
    minitel.clear()

    username, password = "",""

    sel = 0 # username

    q = False
    clear_flag = False
    while not q:
        cr = None

        if clear_flag:
            cr = minitel.ser.read()
            minitel.clear()
            clear_flag = False

        print_form(minitel, username, password)
        minitel.cursorMove(5 + 10 + len(username if sel == 0 else password), 5 + sel)

        if cr is None:
            cr = minitel.ser.read()

        if cr == b'\x1b':
            word = get_word(minitel.ser)

            match word:
                case b'OM':
                    print('Envoi!')
                    print(username)
                    print(password)

                    check_and_print(minitel, username, password)
                    clear_flag = True

                case b'OQ':
                    q = True
                    print("exit")

                case b'[A' | b'[B':
                    print("changing line")
                    sel = 1 - sel


                case _:
                    print('unknown char: '+ str(word))
        else:
            if sel == 0:
                username += cr.decode()
            else:
                password += cr.decode()

