word = []
word = input('단어를 입력해주세요: ')
a = len(word)

for i in range(1,a+1):
    print(word[a-i], end='')
    
-------------------------------------------------------
word = input('단어를 입력해주세요 : ')

# for 변수 in 시퀀스 객체(리스트, 튜플, 문자열, range)
# reversed(시퀀스 객체) 시퀀스 객체를 뒤집어줌

for w in reversed(word):  
    print(w, end = '')
# word에 저장된 문자열에서 요소(문자)를 하나씩 꺼내서 w에 저장하는 것을 word에 있는 모든 요소를 꺼낼 때까지 반복

-----------------------------------------------------
word= input('단어를 입력해주세요 : ')

for w in range((len(word) - 1), -1, -1):
    print(word[w], end = '')
# 좋은 코드는 아닌 것 같지만... 입력한 문자열이 뒤집어져서 출력.
