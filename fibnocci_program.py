#Program for Fibonacci series

a = int(input("Enter the Number for Fibonacci: "))

first = 0
second = 1

for i in range (2, a+1):
    next = first + second
    first = second
    second = next
print(next)




