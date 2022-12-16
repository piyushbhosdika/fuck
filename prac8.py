def ifNumber(arr):
    for item in arr:
        if  not str(item).isnumeric():
          return False
    return True
def countOdd(arr):
    count=0
    if ifNumber(arr):
         for item in arr:
            if item&1:
                count+=1
    return count
def ifString(arr):
    for item in arr:
        if  not str(item).isalpha():
          return False
    return True
def largestString(arr):
    ans="Not Valid String Array"
    ln=0
    if ifString(arr):
        for i in arr:
            if ln<len(i):
              ans=i
              ln=len(i)
    return ans
def reverseList(arr):
    ans=[]
    for i in range(len(arr)-1,-1,-1):
        ans.append(arr[i])
    return ans
def findingKey(key,arr):
    ans=-1
    for i in range(len(arr)):
        if int(arr[i])==key:
          ans=i
    return ans
def removingEle(key,arr):
    arr.remove(str(key))
    return arr
def descendingSort(arr):
    return sorted(arr,reverse=True)
def commonEle(arr1,arr2):
    ans=[]
    arr1=sorted(arr1)
    arr2=sorted(arr2)
    for i in arr1:
        if i in arr2:
          ans.append(i)
    return ans
c=1
while(c<6 and c>0):
    print("*"*50)
    print("\t\t List functions")
    print("*"*50)
    print("\t     1.If all Numbers")
    print("\t     2.Count Odd if Numeric")
    print("\t     3.Largest String")
    print("\t     4.Reverse List")
    print("\t     5.Find a specified element")
    print("\t     6.Remove a specified element")
    print("\t     7.Sort in descending order")
    print("\t     8.Common of two lists")
    print("\t     9.Exit")
    print("*"*50)
    c=int(input(" Enter your choice: "))
    print("*"*50)
    
    if c==1:
        arr=list(input("Enter the list:").split())
        print("The list contains all numbers: ",ifNumber(arr))
    elif c==2:
        arr=list(input("Enter the list:").split())
        print("Number of Odd numbers in Numeric List:",countOdd(arr))
    elif c==3:
        arr=list(input("Enter the list:").split())
        print("Largest String in the string List:",largestString(arr))
    elif c==4:
        arr=list(input("Enter the list:").split())
        print("Reverse form of list:",reverseList(arr))
    elif c==5:
        arr=list(input("Enter the list:").split())
        key=int(input("Enter element to search:"))
        print("Key found at:",findingKey(key,arr))
    elif c==6:
        arr=list(input("Enter the list:").split())
        key=int(input("Enter element to search:"))
        print("Update list after removal:",removingEle(key,arr))
    elif c==7:
        arr=list(input("Enter the list:").split())
        print(sorted(arr,reverse=True))
        # print(arr)
        # print("Sorted list in Descending Order",descendingSort(arr))
    elif c==8:
        arr1=list(input("Enter the list 1:").split())
        arr2=list(input("Enter the list 2:").split())
        print("Common in lists",commonEle(arr1,arr2))
    else:
        exit