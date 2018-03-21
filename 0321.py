inp = input('화씨 온도를 입력하세요 : ')
try:
    f = float(inp)
    cel = (f - 32) * 5.0 / 9.0
    print(cel)
except:
    print("숫자를 입력하세요.")
