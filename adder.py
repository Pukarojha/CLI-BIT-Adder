
#importing from gates
from gates import*

def binaryAdder(firstNum,secondNum):
    k=7
    carry=0
    binaryList=[0,0,0,0,0,0,0,0]
    while k>=0:
        num1=firstNum[k]
        num2=secondNum[k]

        sum_=xorGate(xorGate(num1,num2),carry)
        binaryList[k]= sum_

        #operating logic gates
        
        and1= andGate(num1,num2)
        and2= andGate(xorGate(num1,num2),carry)
        carry= orGate(and1,and2)

        k=k-1

    return binaryList
        
