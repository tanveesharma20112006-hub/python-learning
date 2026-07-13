numbers = [10, 20, 30, 40, 50]
numbers [0] , numbers [-1] = numbers [-1] , numbers [0]
print(numbers)

n=int(input("enter length of list:"))
number = []
for i in range(n):
    x = int(input("enter the list:"))
    number.append(x)
    number [0], number [-1] = number [-1] , number [0]
    print(number)