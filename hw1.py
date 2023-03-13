def get_radius(prompt):
    r=int(prompt)
    return r

def get_circle_area(num1):
    a=3.14*num1*num1
    return a


input_prompt=input('넓이를 구하고자 하는 원의 반지름은? ')
result1=get_radius(input_prompt)
print(result1)
result2=get_circle_area(result1)
print('반지름',end=' ')
print(result1,end='')
print('인 원의 넓이= ',end='')
print(result2)


