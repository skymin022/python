# 가위바위보 게임
# : 컴퓨터랑 가위바위보 게임을 하여, 질 때까지 반복하는 게임을 완성하시오.
# random.choice( 리스트 ) : 리스트 요소중 하나를 랜덤으로 선택
import random
choices = ["가위", "바위", "보"]
win = True
while win:
    computer = random.choice(choices) 
    user = input('가위, 바위, 보 : ')
    print('컴퓨터 : {}'.format(computer))
    print('사용자 : {}'.format(user))
    
    win1 = (user == "가위" and computer == "보" )
    win2 = (user == "바위" and computer == "가위" )
    win3 = (user == "보" and computer == "바위" )
    
    if user == computer:
        win = True
        print("비겼습니다!")
    elif win1 or win2 or win3:
        win = True
        print("이겼습니다!")
    else:
        win = False
        print("졌습니다!")
    

