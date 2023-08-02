import os, main
from printlist import settings_print, settings_hint_change_print, settings_life_change_print

def settings_main():
    while True:
        os.system('cls')
        settings_print()
        _sel = int(input())
        
        if _sel == 1:
            settings_life_change_print()
            _life_change = int(input())
            while(_life_change == 0):
                print("목숨은 하나 이상이어야 합니다.")
                settings_life_change_print()
                _life_change = int(input())
            main._life = _life_change
            
        elif _sel == 2:
            settings_hint_change_print()
            _hint_change = int(input())
            main._hint = _hint_change
            
        elif _sel == 3:
            return