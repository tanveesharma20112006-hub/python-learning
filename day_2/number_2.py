numbers =[1,2,3,4,5]
numbers = []
for i in range(len(numbers)):
    x = int(input("Enter the element:")) 
    numbers.append(x)
    numbers[i] = numbers[i]*2
    print(numbers)
