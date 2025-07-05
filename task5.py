#Q1
num=int(input("enter a number:"))
if(num%2==0):
    print(f"the number {num} is even ")
else:
    print(f"the number {num} is odd ")

#Q2
num1=int(input("enter a number:"))
if(num%5==0 and num%10!=0):
    print(f"the {num1} is satisfy")
else:
    print(f"the {num1} is not satisfy")

#Q3
a=int(input("enter first number:"))
b=int(input("enter second number:"))
if(a>b):
    print("the biggest number is ={a}")
else:
    print("the biggest number is ={b}")

#4Q
A=int(input("enter first number:"))
B=int(input("enter second number:"))
if(A>B):
    print("the  smallest number is ={A}")
else:
    print("the smallest  number is ={B}")

#Q5
num2=int(input("enter a number:"))
if(num%2==0 and num%3==0 and num%6==0):
    print(f"the {num2} is statisfy ")
else:
    print(f"the {num2} is not statisfy ")

#Q6
age=int(input("enter person age:"))
if(age>=18):
    print("person is elgible to vote")
else:
    print("person is not elgible to vote")

#Q7
maths=int(input("enter your marks:"))
physics=int(input("enter your marks:"))
chemistry=int(input("enter your marks:"))
if(maths>=35 and physics>=35 and chemistry>=35):
    print("your pass")
else:
    print("your fail")

#Q8
maths1=int(input("enter your marks:"))
physics1=int(input("enter your marks:"))
chemistry1=int(input("enter your marks:"))
if(maths1>=35 or physics1>=35 or chemistry1>=35):
    print("your pass")
else:
    print("your fail")

#Q9
maths_1=int(input("enter your marks:"))
physics_1=int(input("enter your marks:"))
chemistry_1=int(input("enter your marks:"))
if((maths_1>=35 and physics_1>=35) or (chemistry_1>=35 and maths_1>=35) or (physics_1>=35 and chemistry_1>=35)):
    print("your pass")
else:
    print("your fail")

#Q10
z=int(input("enter a number:"))
y=int(input("enter a number:"))
x=int(input("enter a number:"))
if(z>y and z>x):
    print(f"{z} is biggest number")
elif(y>x):
    print(f"{y} is biggest number")
else:
    print(f"{x} is biggest number")

#11
p=int(input("enter a number:"))
q=int(input("enter a number:"))
r=int(input("enter a number:"))
if(p<q and p<r):
    print(f"{z} is smallest number")
elif(q<r):
    print(f"{y} is smallest number")
else:
    print(f"{x} is smallest number")

#15
year=int(input("enter a year:"))
if(year%4==0 and year%100!=0) or (year%400==0):
    print(f"the {year} is leap year ")
else:
    print(f"the{year} is not a leap year ")

#Q13

members=int(input("enter number of people:"))
if members%5==0:
    cars=members/5
else:
    cars=(members/5)+1 
print("cars needed", cars)

#14
m=int(input("enter first number:"))
n=int(input("enter second number:"))
o=int(input("enter third number:"))
if m>n:
    if m>o:
        if n>o:
            print("second biggest=",n)
        else:
            print("second biggst=",o)
    else:
        print("second biggest=",m)
else:
    if n>o:
        if m>o:
            print("second biggest=",m)
        else:
            print("second biggest=",o)
    else:
        print("second biggest=",n)
       
