import random

com = 0
play = 0 K
while True:
    player = ""
    while True:
        player = input("(가위, 바위, 보) 중에서 하나를 선택하세요. 종료하시려면 <종료>를 입력하세요. : ")
        if player == "종료":
            break
        elif player == "가위" or player == "바위" or player == "보":
            break
        else:
            print("없는 명령 입니다.")
    number = random.randint(0, 2)
    if number == 0:
        computer = "가위"
    elif number == 1:
        computer = "바위"
    else:
        computer = "보"
    print("사용자: ", player, "컴퓨터: ", computer)
    if player == computer:
        print("비겼음!")
    elif player == "바위":
        if computer == "보":
            print("컴퓨터가 이겼음!")
            com += 1
        else:
            print("사용자가 이겼음!")
            play += 1
    elif player == "보":
        if computer == "바위":
            print("사용자가 이겼음!")
            play += 1
        else:
            print("컴퓨터가 이겼음!")
            com += 1
    elif player == "가위":
        if computer == "바위":
            print("컴퓨터가 이겼음!")
            com += 1
        else:
            print("사용자가 이겼음!")
            play += 1
    print("[현재 전적] 컴퓨터 : " + str(com) + " 사용자 : " + str(play))
