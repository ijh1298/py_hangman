import main

def main_print():
    print(f'{"":=^30}')
    print(f'{"Hangman Game":=^30}')
    print(f'{"":=^30}'"\n\n")
    print(f'{"1.":>12}'f'{"시작":^10}')
    print(f'{"2.":>12}'f'{"설정":^10}')
    print(f'{"3.":>12}'f'{"기록":^10}')
    print(f'{"4.":>12}'f'{"종료":^10}')
    print("\n"f'{"":13}'">> ", end='') 
        
def settings_print():
    print("\n\n"f'{"* 설정 *":^30}'"\n")
    print(f'{"현재 목숨 : "}'f'{main._life}'" (기본 값 : 10개)")
    print(f'{"현재 힌트 : "}'f'{main._hint}'" (기본 값 : 0개)")
    print("\n1. 목숨 개수 수정")
    print("2. 힌트 개수 수정") 
    print("3. 메인 화면으로")
    print("\n"f'{"":13}'">> ", end='') 
    
def settings_life_change_print():
    print("목숨 개수 수정 (현재 값 : "f'{main._life}'") \n>> ", end="")

def settings_hint_change_print():
    print("힌트 개수 수정 (현재 값 : "f'{main._hint}'") \n>> ", end="")