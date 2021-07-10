#importing from forInput

from forInput import*

#importing from adder

from adder import*

#importing from conversion
from conversion import*
print("\nName: Pukar Ojha  \nID: 19031809 \nCollege:Itahari International College")
while True:
    r= input("\nPlease enter: \n 1 for Decimal Number \n 2 for Binary Number \n \n Enter the number: ")
    

    if(r=='1'):
        print("***>-----> You Choosed Decimal <-----<***")
        num1,num2= inputDecimal()
        binary1= deciToBinary(num1)
        binary2= deciToBinary(num2)
        result= binaryAdder(binary1, binary2)

    elif(r=='2'):
        print("***>-----> You Choosed Binary<----<***")
        string1, string2= inputBinary()
        binary1= stringToList(string1)
        binary2= stringToList(string2)
        result= binaryAdder(binary1,binary2)

        num1= binaryToDeci(binary1)
        num2= binaryToDeci(binary2)

    elif(r=="" or r==" " or r=="  " or r=="   "):
         print("\n***!!!!Error!!!!*** \n Empty Fields Found!")
         continue
         
    else:
        print("\n***!!!! INVALID INPUT!!!**** \n Please enter appropiate number")
        continue
            

    print("\n")

    print("First Binary Number is : ", listToString(binary1),"||| First Decimal Number is : ",num1)
    print("Second Binary Number is: ", listToString(binary2),"||| Second Decimal Number is: ", num2)
    print("                        +-------   |||                            +---")
    print("Sum in Binary           :",listToString(result), "|||  Sum in Decimal          :  ",(num1+num2))
    print("\n------------------*-------------------*---------------------*----------")
    print("\nDo you want to continue?")
    
    while True:
        print("\nEnter: \n'y' or 'Y' for continue and \n'n' or 'N' for Quit.")
        c= input("\nEnter: ")
        c=c.lower()
        if c=="y" or c=="n":
            break
        elif c=="" or c=="  " or c==" " or c=="   ":
            print("\n***!!! ERROR !!!***","\nEmpty field found ")
            print("\nPlease enter appropiate value")
            continue
        else:
            print("\n***!!!! ERROR !!!!***")
            print("Enter appropiate value")
            continue
    if c=="y":
        continue
    else:
        break
