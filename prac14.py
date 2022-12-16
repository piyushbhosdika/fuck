def writeDataToFile(ifilename): 
    string = input('Enter Data: ')
    while True:
        temp = input()
        if temp:
            string += '\n' + temp
        else:
            break
    fout = open(ifilename, 'w')
    fout.write(string)
    fout.close()
def copyOddLines(ifilename, ofilename): 
    try:

        fin = open(ifilename, 'r')
        fout = open(ofilename, 'w') 
        data = fin.readlines()
        for i in range(0, len(data), 2):
            fout.write(data[i])
        fin.close()
        fout.close()
    except FileNotFoundError as e:
        print(f'Error: {ifilename} was not found.')
exists = input("Does the file exist (y/n)? ") == 'y' 
if exists:

    file1 = input("Enter Input Filename: ") 
else:
    file1 = input("Enter Filename to Write Data: ")
    writeDataToFile(file1)
file2 = input("Enter Output Filename: ") 
copyOddLines(file1, file2)