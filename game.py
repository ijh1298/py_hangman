import os, main, nltk, random, record

def game_main():
    nltk.download('words')

    from nltk.corpus import words
    word_list = words.words()
    while True:
        __life = main._life
        __hint = main._hint
        
        used_characters = []

        random_word = random.choice(word_list)
        random_word = random_word.lower()
        
        os.system('cls')
        
        current_word = "__________________________________________________"
        _len_random_word = len(random_word)
        hint_word = random_word[random.randrange(0, _len_random_word - 1)]
        
        _msg = -1
        
        while True:
            if _msg == 0:
                print('*한 글자 또는 전체 단어를 입력해야 합니다.*')
            elif _msg == 1:
                print('*이미 입력한 단어입니다.*')
            elif _msg == 2:
                print('*힌트 단어 : 'f'{hint_word}''*')
            elif _msg == 3:
                print('!힌트를 사용할 수 없습니다!')
            
            _msg = - 1
            #정답 종료
            if (current_word[:_len_random_word] == random_word):
                record.record_write(0, random_word)
                print('정답 : 'f'{random_word}'' 맞았습니다!\n\n')
                print('다시 하시겠습니까? (Y/N) >>', end = " ")
                re = input()
                if re == 'y' or re == 'Y':
                    break;
                return
            #목숨 종료
            if (__life <= 0):
                record.record_write(1, random_word)
                print('정답 : 'f'{random_word}'' 틀렸습니다...\n\n')
                print('다시 하시겠습니까? (Y/N) >>', end = " ")
                re = input()
                if re == 'y' or re == 'Y':
                    break;
                return
            
            #게임 디스플레이
            print("\n""단어 길이 : "f'{_len_random_word}')
            print(f'{"목숨":>20}'" : "f'{__life}')
            print(f'{"힌트":>20}'" : "f'{__hint}'"\n")
            for i in range(0, _len_random_word):
                print(current_word[i], end= " ")
            print("\n틀린 단어 : ", end = "")
            print("")
            used_characters.sort()
            for c in used_characters:
                print(c, end = " ")
            if __hint > 0:
                print("\n#힌트 사용하려면 숫자 0 입력#", end="")
            print("\n>>", end = " ")
            
            #단어 입력부
            input_char = input().lower()
            _len_input_char = len(input_char)
            
            #msg 0 : 글자 하나 또는 전체만 입력 가능
            if _len_input_char != 1 and _len_input_char != _len_random_word:
                _msg = 0
            #msg 1 : 이미 입력한 단어
            elif input_char in used_characters or input_char in current_word:
                _msg = 1
            #msg 2 : 힌트 사용, msg 3 : 힌트 사용 실패
            elif input_char == '0':
                if __hint > 0 :
                    __hint -= 1
                    _msg = 2
                    while hint_word in current_word:
                        hint_word = random_word[random.randrange(0, _len_random_word)]
                else :
                    _msg = 3
            else:    
                #입력한 단어가 속해있는지 확인
                _find = random_word.find(input_char)
                find_list = []
                
                #없음
                if _find == -1:
                    __life -= 1
                    used_characters.append(input_char)
                #있음
                else:
                    find_list.append(_find)
                    while _find != -1:
                        _find = random_word.find(input_char, _find + 1)
                        if _find != -1:
                            find_list.append(_find)
                    for i in find_list:
                        current_word = current_word[:i] + input_char +current_word[i + 1:]
                        
            os.system('cls')