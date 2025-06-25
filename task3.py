#write a program to find the simple interest with using formula
price=int(input("enter the price:"))
time=int(input("enter the time:"))
rate=int(input("enter the rate:"))
sim_int=(price*time*rate)/100
print(f"simple interest is {sim_int}")

#temperature conversion (celsius to farenheit)
cel=input("enter celsius:")
farenheit=(int(cel)*9/5)+32
print(farenheit)

#find the average of three numbers 
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
avg=(a+b+c)/3
print(f"average of three numbersis{avg}")

#write a program a calculate area of circle 
rad=input("enter radius:")
area=3.14*(int(rad)**2)
print(f"area of circle is {area}")
