def get_fixed_price(discounted_price):
    return (discounted_price*((100+rate)/100))
    
rate=int(input('할인율은? '))
Aprice=int(input('A 상품의 할인된 가격은? '))
Bprice=int(input('B 상품의 할인된 가격은? '))
print('A 상품의 정가는 ',get_fixed_price(Aprice),'원')
print('B 상품의 정가는 ',get_fixed_price(Bprice),'원')
