def readTotalContent():
    file = open('data.txt','r')

    content = file.read()  
    print(content)

    file.close() #always close the file

def readLineByLine():
    file = open('data.txt','r')
    line = file.readline()
    while line:
        line = file.readline()     # Read one line
        print(line)

    file.close()

def readAllLines():
    file = open('data.txt','r')

    lines = file.readlines() 
    print(lines)

    file.close()

def readWith():
    """ Does Not Required To Use Close()"""
    with open('data.txt','r') as file:
        line = file.read()
        while(line):
            print(line)
            line = file.read()


def WriteInFile():

    file = open('data.txt','a')
    file.write("This is Last Line !!! Append Through File.py")
    file.close()

readWith()