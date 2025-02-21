def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-2)+fibo(n-1)
    
result=fibo(5)
print(result)


def f(liste,name):
    if len(liste)==0:
        return 0
    return liste[0]+f(liste[1:])
