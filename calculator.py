print("-----------------welcome to calculator------------------")
print("select operation ")
print("1 + sum")
print("2 - subtract")
print("3 * multiply")
print("4 / division")
choose = (input("Enter choise 1/2/3/4 -"))
a = float(input("Enter first number: "))

b = float(input("Enter second number: "))


if choose =="1":
    print(a+b)

elif choose =="2":
    print(a-b)

elif choose =="3":
    print(a*b)

elif choose =="4":
    print(a/b)        

else:
    print("Invalid chooise")
