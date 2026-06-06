#1  check positive negative or zero
no=int(input("enter your no:"))
if no>0:
    print("your no is a positive no")
elif no==0:
    print("your no is 0")
else:
    print("your no is negative")
#2 check odd or even
no=int(input("enter your no:"))
if no%2==0:
    print("your no is a even no"))
else:
    print("your no is a odd no"))
#3 largest of two no:
no1=int(input("enter your first no"))
no2=int(input("enter your second no"))
if no1>no2:
    print("your first no is the greatest no:")
elif no1==no2:
    print("both are equal no")
else:
    print("your second no is the greatest")
#4 vote eligiblity
age=int(input("enter your age"))
if age>=18:
    print("you are eligible for votting")
else:
    print("you are not eligible for votting")
#5 pass or fail
mark=int(input("enter your marks"))
if mark>=35:
    print("You are pass")
else:
    print("you are fail")
#6 pasword checker
password=input("enter your password")
if password=='mahilan9':
    print("correct password")
else:
    print("try  again wrong password")
    
    
