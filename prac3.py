def fibo(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return(fibo(n-1)+fibo(n-2))
def fact(n):
    if n==1 or n==0:
      return 1
    return n*fact(n-1)
def findFiboFact(n):
    return [fibo(n),fact(n)]


