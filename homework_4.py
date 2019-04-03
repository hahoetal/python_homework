price = input('가격을 입력해주세요: ')
discount_rate = input('할인율을 입력해주세요: ')

price = int(price)
discount_rate = int(discount_rate)

discount_price = price * (100 - discount_rate) /100

print('할인된 가격은',discount_price, '입니다.')
