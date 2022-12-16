def length():
    st = input(" Ënter string: ")
    print(" Length of string : ",len(st))
def max3():
    st = input(" Ënter string 1: ")
    st1 = input(" Ënter string 2: ")
    st2 = input(" Ënter string 3: ")
    print(" Max of 3 strings : ",max(st,max(st1,st2)))
def replaceVowels():
    st = input(" Ënter string: ")
    ans=""
    for i in range(len(st)):
        if st[i].lower() in "aeiou":
            ans+="#"
        else:
            ans+=st[i]
    print(" String without vowels: ",ans)
def countWords():
    st = input(" Ënter string: ")
    li=st.split()
    print(" No. of words: ",len(li))
def isPalindrome():
    st = input(" Ënter string: ")
    ans=""
    for i in range(len(st)-1,-1,-1):
        ans+=st[i]
    if st.lower()==ans.lower():
        print("Yes,The entered string is a palindrome")
    else:
        print("No,The entered string is not a palindrome")
        
c=1
while(c<6 and c>0):
    print("*"*50)
    print("\t\t Strings functions")
    print("*"*50)
    print("\t     1.Length of string")
    print("\t     2.Max of 3 strings")
    print("\t     3.Replace vowels")
    print("\t     4.Count words")
    print("\t     5.Palindrome check")
    print("\t     6.Exit")
    print("*"*50)
    c=int(input(" Enter your choice: "))
    print("*"*50)
    if c==1:
        length()
    elif c==2:
        max3()
    elif c==3:
        replaceVowels()
    elif c==4:
        countWords()
    elif c==5:
        isPalindrome()
    else:
        break



# def lenOfString(str):
#     count=0
#     for i in len(str):
#         if str[i]!=" ":
#             count+=1
#     return count