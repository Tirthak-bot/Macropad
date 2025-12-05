import Board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys

keyboard = KMKKeyboard()


display = Display(
    display=SSD1306(sda=board.D4, scl=board.D5),
    entries=[
        TextEntry(text='HOLA! :3'),
    ],
    height=80,
)
keyboard.extensions.append(display)


keyboard.col_pins = (board.D7, board.D6, board.D3)
keyboard.row_pins = (board.D8, board.D9, board.D10)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


keyboard.modules.append(encoder_handler)

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.D1, board.D2, board.D0),)
encoder_handler.map = (((KC.VOLD, KC.VOLU, L1_KEY),), 
                       ((KC.VOLD, KC.VOLU, KC.TRNS),),)


keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(MouseKeys())

keyboard.keymap = [

    [     
        KC.N1,  KC.N2,   KC.N3,
        KC.N4,  KC.N5,   KC.N6, 
        KC.N7,  KC.N8,   KC.N9,
    ],

    [
        KC.MPRV,   KC.MPLY,  KC.MNXT,
        KC.MUTE,   KC.BRID,  KC.BRIU,
        KC.MB_LMB,  KC.MB_MMB,  KC.MB_RMB,
    ]
]



if __name__ == '__main__':
    keyboard.go()