# Writeafunctionthattakesthelengthsofthreesides:side1,side2andside3of thetriangleastheinputfrom theuserusinginputfunctionandreturnthearea andperimeterofthetriangleasatuple.Also,assertthatsum ofthelengthofany twosidesisgreaterthanthethirdside.

def func1():
    s1=int(input("Enter 1st side:"))
    s2=int(input("Enter 2nd side:"))
    s3=int(input("Enter 3rd side:"))
    perimeter=s1+s2+s3
    if not(s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1):
        print("Invalid sides.")
        exit()
    s=perimeter/2
    area=((s)*(s-s1)*(s-s2)*(s-s3))**(1/2)
    res=(perimeter,round(area,2))
    print(res)

func1()