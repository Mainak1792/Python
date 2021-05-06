print("enter_your_number")
num=int(input())
rev=0
n=0
while(num>0):
   n=num%10
   rev=n+rev*10
   num=int(num/10)
print(rev)
if (num == rev):
    print("palindrome")
