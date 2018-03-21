try:
    h = float(input('Enter your Score: '))
    if h >= 0.9:
        print('A')
    elif h >= 0.8:
        print('B')
    elif h >= 0.7:
        print('C')
    elif h >= 0.6:
        print('D')
    elif h < 0.6:
        print('F')
except:
    print("입력에 오류가 발생하였습니다. 범위는 0.0 ~ 1.0입니다.")
