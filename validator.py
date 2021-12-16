

def operaciya(s):
    def wrapper(a,b):
        if a==2:
           print( 'Сумма:' )
           s(a,b)
        else:
           print( 'ERROR' )
    return wrapper

@operaciya
def summa(a,b):
    c=a+b
    print(c)


summa(3,3)