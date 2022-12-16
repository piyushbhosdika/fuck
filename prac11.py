def linerSearch(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1
def binarySearch(arr,key):
    arr=sorted(arr)
    s=0
    e=len(arr)-1
    while s<e:
        mid=(s+e)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            e=mid-1
        else:
            s=mid+1
    return -1
def bubbleSort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr
def insertionSort(arr):
    for i in range(1,len(arr)+1):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
    return arr
    
def selectionSort(arr):
    for i in range(len(arr)):
        minpos=i
        for j in range(1,len(arr)+1):
            if arr[j]<arr[minpos]:
                minpos=j
        temp=arr[i]
        arr[i]=arr[minpos]
        arr[minpos]=temp
    return arr

c=1
while(c<6 and c>0):
    print("*"*50)
    print("\t\t List functions")
    print("*"*50)
    print("\t     1.Linear Search an element")
    print("\t     2.Binary Search an element")
    print("\t     3.Bubble Sort the list")
    print("\t     4.Insertion Sort the list")
    print("\t     5.Selection Sort the list")
    print("\t     6.Exit")
    print("*"*50)
    c=int(input(" Enter your choice: "))
    print("*"*50)
    
    if c==1:
        arr=list(input("Enter the list:").split())
        key=input("Enter element to search:")
        print("Key found at:",linerSearch(arr,key))
    elif c==2:
        arr=list(input("Enter the list:").split())
        key=input("Enter element to search:")
        print("Key found at:",binarySearch(arr,key))
    elif c==3:
        arr=list(input("Enter the list:").split())
        print("List after Bubble Sort:",bubbleSort(arr))
    elif c==4:
        arr=list(input("Enter the list:").split())
        print("List after Insertion Sort:",insertionSort(arr))
    elif c==5:
        arr=list(input("Enter the list:").split())
        print("List after Selection Sort:",selectionSort(arr))
    else :
       exit