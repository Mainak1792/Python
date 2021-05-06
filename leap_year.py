print("enter year")
y=int(input())
if y%4==0 and y%100!=0:
    print("ola_das_ist_leap_year\n")
elif y%400==0:
    print("ola_das_ist_leap_year\n")
else:
    print("not_a_leap_year\n")
