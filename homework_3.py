word = []
word = input('단어를 입력해주세요: ')
a = len(word)

for i in range(1,a+1):
    print(word[a-i], end='')
    
