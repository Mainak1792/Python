print("press 1 for addition")
print("press 2 for subtraction")
print("press 3 for Multiplication")
print("press 4 for division")
print("press 5 to stop")
ch=int(input())
if ch>=1 and ch<=4:
    print("enter two number")
    num1=int(input())
    num2=int(input())
    if ch==1:
        result=num1+num2
        print(result)
    if ch==2:
        result=num1-num2
        print(result)
    if ch==3:
        result=num1*num2
        print(result)
    if ch==4:
        result=num1//num2
        print(result)
else:
    print("calculator_stopped")
