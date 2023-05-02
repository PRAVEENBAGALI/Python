#Program for factorial of number

a = int(input("Enter the number for factorial: "))
f =1

if a < 0:
    print("factorial is not possible")
elif a == 0:
    print("factorial is 1")
else:
    for a in range (1,a+1):
        f = f * a
    print(f)