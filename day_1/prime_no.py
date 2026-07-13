num = int(input("Enter the number:"))
if num > 1:
    prime = True
    for i in range(2,num):
        if num % i == 0:
            prime = False
            break;
if prime:
    print("This number is prime")
else :
    print("This is not a prime number")
    