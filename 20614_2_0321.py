try:
    h = int(input('Enter Hours : '))
    r = int(input('Enter Rate : '))
    if h >= 40:
        print('Pay : ' + str(40 * r + (h - 40) * r * 1.5))
    else:
        print('Pay : ' + str(h * r))
except:
    print("입력에 오류가 발생하였습니다. 숫자만 입력할 수 있습니다.")
