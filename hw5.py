def read_single_digit(c):
    if c==1:
        return '일'
    elif c==2:
        return '이'
    elif c==3:
        return '삼'
    elif c==4:
        return '사'
    elif c==5:
        return '오'
    elif c==6:
        return '육'
    elif c==7:
        return '칠'
    elif c==8:
        return '팔'
    elif c==9:
        return '구'
    else:
        return '영'

def read_number(n):
    if n>=900:
        a=int(n/100)
        b=int((n-100*a)/10)
        c=int(n-(100*a+10*b))
        hund=read_single_digit(a)
        ten=read_single_digit(b)
        one=read_single_digit(c)
        print(f'{hund} {ten} {one}')
    elif n>=800:
        a=int(n/100)
        b=int((n-100*a)/10)
        c=int(n-(100*a+10*b))
        hund=read_single_digit(a)
        ten=read_single_digit(b)
        one=read_single_digit(c)
        print(f'{hund} {ten} {one}')
    elif n>=700:
        a=int(n/100)
        b=int((n-100*a)/10)
        c=int(n-(100*a+10*b))
        hund=read_single_digit(a)
        ten=read_single_digit(b)
        one=read_single_digit(c)
        print(f'{hund} {ten} {one}')
    elif n>=600:
        a=int(n/100)
        b=int((n-100*a)/10)
        c=int(n-(100*a+10*b))
        hund=read_single_digit(a)
        ten=read_single_digit(b)
        one=read_single_digit(c)
        print(f'{hund} {ten} {one}')
    elif n>=500:
        a=int(n/100)
        b=int((n-100*a)/10)
        c=int(n-(100*a+10*b))
        hund=read_single_digit(a)
        ten=read_single_digit(b)
        one=read_single_digit(c)
        print(f'{hund} {ten} {one}')
    elif n>=400:
        a=int(n/100)
        b=int((n-100*a)/10)
        c=int(n-(100*a+10*b))
        hund=read_single_digit(a)
        ten=read_single_digit(b)
        one=read_single_digit(c)
        print(f'{hund} {ten} {one}')
    elif n>=300:
        a=int(n/100)
        b=int((n-100*a)/10)
        c=int(n-(100*a+10*b))
        hund=read_single_digit(a)
        ten=read_single_digit(b)
        one=read_single_digit(c)
        print(f'{hund} {ten} {one}')
    elif n>=200:
        a=int(n/100)
        b=int((n-100*a)/10)
        c=int(n-(100*a+10*b))
        hund=read_single_digit(a)
        ten=read_single_digit(b)
        one=read_single_digit(c)
        print(f'{hund} {ten} {one}')
    elif n>=100:
        a=int(n/100)
        b=int((n-100*a)/10)
        c=int(n-(100*a+10*b))
        hund=read_single_digit(a)
        ten=read_single_digit(b)
        one=read_single_digit(c)
        print(f'{hund} {ten} {one}')
    else:
        b=int(n/10)
        c=int(n-10*b)
        ten=read_single_digit(b)
        one=read_single_digit(c)
        print(f'{ten} {one}')
        

input_n=int(input('세 자리 정수 입력: '))
read_number(input_n)


    
    
