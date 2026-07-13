#else
try:
    x = int(input("Enter a number:"))
except ValueError:
    print ("invalid input")
else:
    print("you entered",x)

#raise
age = int(input("Enter your age:"))
if age < 0:
    raise ValueError ("Age cannot be negative")

#finally
try:
    x = int(input("Enter a number:"))
except ValueError:
    print("invalid input")
finally:
    print ("Program Finished")