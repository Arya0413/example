'''write a python code to check whether the input year is leap year or not
hint: A leap year is exactly divisible by 4 excpet for century years ending with 00
    A century year is leap year only if it is perfectly divisible by 400'''
a=int(input("Enter the year : "))
if(a%100==0):
    if(a%400==0):
        print(a," is a leap year")
    else:
        print(a," is not a leap year")
elif(a%4==0):
    print(a," is a leap year")
else:
    print(a," is not a leap year")
    
