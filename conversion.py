
#converting decimal to binary
def deciToBinary(decimal):
    k= 7
    list_=[0,0,0,0,0,0,0,0]
    
    while decimal>0:
        remainder= decimal %2
        list_[k]= remainder
        decimal= int(decimal/2)

        k-=1

    return list_

#converting list to string
def listToString(list_):
    binary=""
    
    for r in range(8):
        binary+= str(list_[r])
    return binary

#converting string to list
def stringToList(string):
    list_=[0,0,0,0,0,0,0,0,]
    p=7
    
    for i in range(len(string)-1,-1,-1):
        list_[p]= int(string[i])

        p-=1

    return list_


#converting binary to decimal
def binaryToDeci(binaryList):
    decimal=0
    power= 0
    k=7
    while k>=0:
        decimal= decimal+ (binaryList[k]*(2**power))
        power+= 1
        k-= 1
    return decimal    
