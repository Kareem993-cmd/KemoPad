import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.rgb import RGB

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

rgb = RGB(
    pixel_pin=board.D6,
    num_pixels=2,
    val_limit=40,
    hue_default=180,
    sat_default=255,
    val_default=40
)
keyboard.modules.append(rgb)

PINS = [board.D1, board.D2, board.D3, board.D4]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.A,
        KC.MACRO("Hello World!"),
        KC.Macro(Press(KC.LCTRL), Tap(KC.S), Release(KC.LCTRL)),
        KC.DELETE,
    ]
]

if __name__ == '__main__':
    keyboard.go()
