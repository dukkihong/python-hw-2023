shopping_bag={}
print('[구입]')
while True:
    i=str(input('상품명? '))
    if i=='':
        break
    j=int(input('수량은? '))
    shopping_bag[i]=j
    print(f'장바구니에 {i}가(이) {j}개 담겼습니다.\n')


print(f'\n>>>장바구니 보기: {shopping_bag}\n')

print('[검색]')
p=str(input('장바구니에서 확인하고자 하는 상품은? '))
q=shopping_bag.get(f'{p}')
print(f'{p}은(는) {q}개 담겨 있습니다.')
    
