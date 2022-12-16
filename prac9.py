def highestPercentage(n):
    mx=0
    mxName=""
    for item in range(n):
        name=input("Enter name of the #{} student: ".format(item+1))
        eng=int(input("Enter English marks of the #{} student: ".format(item+1)))
        mat=int(input("Enter Maths marks of the #{} student: ".format(item+1)))
        sci=int(input("Enter Science Marks of the #{} student: ".format(item+1)))
        sst=int(input("Enter Social Studies marks of the #{} student: ".format(item+1)))
        perc=(eng+mat+sci+sst)/4
        dict={name:[[eng,mat,sci,sst],perc]}
        
        for i in range(len(dict)):
            if dict[name][i]>mx:
                mx=perc
                mxName=name
    return mxName
n=int(input("Enter the number of students: "))
print("Student With highest percentage is :",highestPercentage(n))