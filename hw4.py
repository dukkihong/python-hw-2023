def get_length(msg1,msg2):
    nstr=len(msg1) if(len(msg1)>len(msg2)) else len(msg2)
    return nstr

def draw_line_string(name):
    msg1=f'Hello {name},'
    msg2=f'Welcome to Seoul.'
    print('-'*get_length(msg1,msg2))
    print(msg1)
    print(msg2)
    print('-'*get_length(msg1,msg2))

input_name=input('his/her name: ')
draw_line_string(input_name)

