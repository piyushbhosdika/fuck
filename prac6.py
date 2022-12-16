t1= (1,3,5,7,9,2,4,6,8,10)
t2= (11,13,15)
def a(t1):
    ans=()
    for i in t1:
        if i%2==0:
            ans=ans+(i,)
    print(ans)
a(t1)
def b(t1,t2):
    return(t1+(t2))
print(b(t1,t2))
def c(t1):
    print("Maximum element is: ",max(t1))
    print("Minimum element is: ",min(t1))
c(b(t1,t2)) 

