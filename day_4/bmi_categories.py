height = float(input("height:"))
weight = float(input("weight:"))
bmi = weight/(height**2)
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")