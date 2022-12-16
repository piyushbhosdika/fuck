from prac3 import fact
def series(x,n):
    sum=1
    for item in range(1,n,1):
        if item%2==1:
            sum-=(x**(2*item))/fact(2*item)
        else:
            sum+=(x**(2*item))/fact(2*item)
    return sum
print(series(1,3))
