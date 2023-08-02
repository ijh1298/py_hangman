import os, sys, settings, game, record
from printlist import main_print

_life = 10
_hint = 0

def run():
    while True:
        os.system('cls')
        main_print()
        _sel = input()
        
        if _sel == '1':
            game.game_main()
        elif _sel == '2':
            settings.settings_main()
        elif _sel == '3':
            record.record_read()
        elif _sel == '4':
            print("행맨 게임을 종료합니다.")
            sys.exit()
        else:
            pass

if __name__ == "__main__":
    run()