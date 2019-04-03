num = input('숫자를 입력해주세요: ')
num = int(num)

for a in range(1, num+1):
    if 0 < a < num:
        print('*' * a)
    else :
        print('*' * num)
