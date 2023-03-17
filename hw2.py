def exchange(prompt):
    num500= prompt // 500
    prompt %= 500

    num100= prompt // 100
    prompt %= 100

    num50= prompt // 50
    prompt %= 50

    num10= prompt // 10

    print('500원 동전의 개수:',num500)
    print('100원 동전의 개수:',num100)
    print('50원 동전의 개수:',num50)
    print('10원 동전의 개수:',num10)

def get_integer(a):
    res=int(input(a))
    return res

input_a=get_integer('동전으로 교환하고자 하는 금액은? ')
exchange(input_a)
