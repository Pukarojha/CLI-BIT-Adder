#calling all the function from conversion file

from conversion import*

def  inputDecimal():
    print(">----> Enter the positve deimal numbers, less than 256 here <----<")

    while True:
        while True:
            try:
                firstNum= int(input("\n Enter the first decimal number: "))
                if firstNum<0:
                    print("\n!!!! ERROR !!!!")
                    print("\nDecimal Numbers are expected to be greater than or equal to  0")
                    print("\nPlease enter positive number")
                    continue
                elif firstNum>255:
                    print("\n!!!! ERROR !!!!")
                    print("\nDecimal Numbers are expected to be less than 256")
                    continue
                else:
                    break
                break
            except ValueError:
                print("\n!!!! ERROR !!!!")
                print("\nDecimal Numbers are expected to be less than 256 and greater than or equal to 0")
                print("\ni.e. 256>Decimal Numbers>0")
                print("\nPlease enter valid Decimal Number")
                continue
        while True:
            try:
                secondNum= int(input("\n Enter the second number: "))
                if secondNum<0:
                    print("\n!!!! Error !!!!")
                    print("\nDecimal Numbers are expected to be greater or equal to 0")
                    print("\nPlease enter positive number")
                    continue
                elif secondNum>255:
                    print("\n!!!! ERROR !!!!")
                    print("Decimal Numbers are expected to be less than 256")
                    continue
                else:
                    break 
                break

            except ValueError:
                print("\n!!!! ERROR !!!!")
                print("\n Decimal Numbers are expected to be less than 256 and greater than or equal to 0")
                print("\ni.e. 256<Decimal Numbers>=0")
                print("\nPlease enter valid Decimal Number")
                continue

                

#validation for output
#since,this program is byte adder it only support bytes

        if firstNum+secondNum>255:
            print("\n!!!! ERROR !!!!")
            print("\nSince,this is the byte adder program. So,")
            print("the sum of two numbers must be less than 256")
            continue
        else:
            break
        break
    return firstNum,secondNum
            
def inputBinary():
    j=">----> Enter Binary Number, here <----<"
    print(j)
    print("\nBinary Number are the combination of two digits 0 and 1")
    print("\nNote:", "\n Minimium Binary Number should be 8-bits zero","\ni.e. 00000000")
    print("\n Maximium Binary Number should be 8-bits one","i.e. 11111111")

    while True:
        while True:
            firstNum=input("\n Enter the first Binary Number: ")
            num1= 0
            length =len(firstNum)

            if length>8:
                print("\n ****!!!! ERROR !!!!**** \n The input, Binary Number should be 8-bits integer")
                print("\n")
                continue
            elif firstNum=="" or firstNum==" " or firstNum=="  " or firstNum=="   ":
                print("\n!!!! ERROR !!!! \n !!!Fields are empty!!! ")
                print("\n")
                continue
            else:
                try:
                    #converting string num into integer
                    num1=int(firstNum)
                    
                    #converting int to list
                    list_= list(map(int,str(num1)))

                    #converting list to set
                    set_=set(list_)
                    if set_=={0} or set_=={1} or set_=={0,1}:
                        break
                    else:
                        print("\n!!!! ERROR !!!!")
                        print("\n Make sure inputs are combination of 0 and 1 only")
                        continue
                except ValueError:
                    print("\n !!!!ERROR !!!!","\n !!! INVALID INPUT !!!")
                    print("\n Please enter Binary Numbers","\nNumbers made by combination of 0 and 1")
                    continue

        while True:
                secondNum=input("\n Enter the second Binary Number: ")
                num2=0
                length=len(secondNum)

                if length>8:
                    print("\n !!!! ERROR !!!!")
                    print("\n The input, Binary Number must be 8-bits integer ")
                    continue
                elif secondNum=="" or secondNum==" " or secondNum=="  " or secondNum=="   " :
                    print("\n!!!! ERROR !!!!")
                    print("\n !!! Fields are empty !!!")
                    continue
                else:
                    try:
                        #converting string num to integer
                        num2= int(secondNum)

                        #converting int to list
                        list_=list(map(int,str(num2)))

                        #converting list to set
                        set_= set(list_)
                        if set_=={0} or set_=={1} or set_=={0,1}:
                            break
                        else:
                            print("\n!!!! ERROR !!!! \n Make sure inputs are combination of 0 and 1 only")
                            print("\n")
                            continue
                    except ValueError:
                        print("\n ****!!!! ERROR !!!!****","\n !!! INVALID INPUT !!! ")
                        print("\n Please enter Binary Numbers","\n Numbers with the combination of 0 and 1 only")
                        continue
                
                    
    #converts string to list
        firstList= stringToList(firstNum)
        secondList= stringToList(secondNum)

        #conveting list to int
        decimal1= binaryToDeci(firstList)
        decimal2=binaryToDeci(secondList)

        if decimal1 + decimal2 >255:
            print("\n!!!! ERROR !!!!")
            print("\n Sum of these two numbers should not exceed a byte")
            continue
        else:
            break

    return firstNum,secondNum
                
               
            
                        
                    
                    
                    
            
    
