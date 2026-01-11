class MinitelCode:
    TEXT = 'TEXT'
    ENVOI = 'ENVOI'
    SOMMAIRE = "SOMMAIRE"
    ANNULATION = "ANNULATION"
    RETOUR = "RETOUR"
    REPETITION = "REPETITION"
    GUIDE = 'GUIDE'
    CORRECTION = "CORRECTION"
    SUITE = "SUITE"
    MOVE_UP = "MOVE UP"
    MOVE_DOWN = "MOVE DOWN"
    MOVE_RIGHT = "MOVE RIGHT"
    MOVE_LEFT = "MOVE LEFT"
    GO_BACK_UP = "GO BACK UP"
    INSERT_LINE = "INSERT LINE"
    SUPPR_LINE = "SUPPR LINE"
    SUPPR_COLUMN = "SUPPR COLUMN"
    INSERT_COLUMN = "INSERT COLUMN"
    E_Page = "E.Page"
    CONNEXION = "CONNEXION"
    BS = "BS"
    LF = "LF"
    CAN = "CAN"
    TAB = "TAB"
    BRK = "BRK"
    DELETE = "DELETE"
    CARRIAGE_RETURN = "CARRIAGE RETURN"
    UNKNOWN_CODE = "UNKNOWN CODE"

class MinitelInput:
    code: str
    text: str

    def __init__(self, code: str, text: str = ""):
        self.code = code
        self.text = text

