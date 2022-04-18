import math
import hashlib
from sys import argv

arrBin1 = []
arrBin2 = []
integers = []

def readFromFile():
    file = open(argv[1], 'r')
    for line in file.readlines():
        line = line.strip("\n")  
        integers.append(int(line))
    file.close()

def calcl():
    n = len(integers)
    m = integers[-1]
    l = math.ceil(math.log(m/n))
    return l

def createLArray():
    l = calcl()
    for i in range(len(integers)):
        int2bin = (bin(integers[i]))
        arrBin1.append(int(int2bin[-int(l):]))
    L = bytearray(arrBin1)
        
    return L

def createUArray():
    l = calcl()
    n = len(integers)
    for i in range(len(integers)):
        int2bin = (bin(integers[i]))
        arrBin2.append(int(int2bin[(int(n)-int(l)):]))
    U = bytearray(arrBin2)  

    return U


def main():
    readFromFile()
    L = createLArray()
    U = createUArray()

    hashLU = hashlib.sha256()
    hashLU.update(L)
    hashLU.update(U)
    digest = hashLU.hexdigest()
    
    print("Number l equals to:", calcl())
    print("Array L:", L)
    print("Array U:", U)
    print("Hash is:", digest)
    

if __name__ == "__main__":
    main()
