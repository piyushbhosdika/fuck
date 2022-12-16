s=input("Enter the string: ")
dict={}
for i in s:
    dict[i]=0
for i in s:
    dict[i]+=1
for i in dict.keys():
    print("Frequency of {} in {} is: ".format(i,s),dict[i])