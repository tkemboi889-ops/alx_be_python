num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
operation=input("choose the operation (+,-,*,/):")

result="result"
match operation:

    case"+":
        
        result=num1+num2
        print()

    case"-":
        result=num1-num2
    case"*":
        
        result=num1*num2
    case"/":
        
        result=num1/num2
        if num1/0:
            print("cannot divide by zero")
        else:
            print("",result)
    case _:
            print("no operation done")
            print("The result is:",result)
        
