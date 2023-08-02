import os

def record_read():
    while True:
        _check_r = 0
        _check_w = 0
        
        os.system('cls')
        if os.path.exists("right_words.txt"):
            file_right_words = open("right_words.txt", 'r')
            _right_words = file_right_words.readlines()
            
            print('\n*맞은 단어*')
            print(_right_words)
                
            file_right_words.close()
        else:
            print("맞은 단어 파일이 없습니다.")
            _check_r = 1

        if os.path.exists("wrong_words.txt"):
            file_wrong_words = open("wrong_words.txt", 'r')
            _wrong_words = file_wrong_words.readlines()

            print('\n\n*틀린 단어*')
            print(_wrong_words)
                
            file_wrong_words.close()
        else:
            print("틀린 단어 파일이 없습니다.")
            _check_w = 1
        
        if _check_r == 1 and _check_w == 1:
            print('\n혹시 아직 게임을 플레이하지 않으셨나요?')
            print('플레이 후에도 되지 않는다면 초기화를 진행해보세요.')
            print('혹은 실행 폴더 안에 right_words.txt, wrong_words.txt가 있는지 확인하세요!')
        print('\n\n1. 기록 초기화하기')
        print('2. 메인 화면으로 \n>>', end=" ")
        _sel = input()
        if _sel == '1':
            print('정말 초기화 하시겠습니까? (Y/N)')
            while True:
                print('\n>>', end=" ")
                __sel = input()
                if __sel == 'y' or __sel == 'Y':
                    record_init()
                    break
                elif __sel == 'n' or __sel == 'N':
                    break
                else:
                    pass
        elif _sel == '2':
            return
        else:
            pass


def record_write(type, words):
    if type == 0:
        file_right_words = open("right_words.txt", 'a')
        file_right_words.write(words + ' ')
        file_right_words.close
    if type == 1:
        file_wrong_words = open("wrong_words.txt", 'a')
        file_wrong_words.write(words + ' ')
        file_wrong_words.close

def record_init():
    file_right_words = open("right_words.txt", 'w')
    file_right_words.close
    file_wrong_words = open("wrong_words.txt", 'w')
    file_wrong_words.close