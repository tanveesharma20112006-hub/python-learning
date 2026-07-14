
english = int(input("Enter your english score:"))
Hindi = int (input("Enter your hindi score:"))
social_studies = int(input("Enter your sst score:"))
mathematics = int(input("Enter your maths score:"))
science = int(input("Enter your science score:"))
marks =[english,Hindi,social_studies, mathematics,science]
print(marks)
avg_marks = (english + Hindi + social_studies + mathematics + science)/5
print ("your avg marks is:", avg_marks)
total  = (english + Hindi + social_studies + mathematics + science)
if avg_marks < 90:
    print("your avg score is : ", avg_marks  ,"and your grade is A")
elif avg_marks < 75:
    print("your avg score is : ",  avg_marks ,"and your grade is B")   
elif avg_marks < 50:
    print("your avg score is :" , avg_marks , "and your grade is C ") 
else :
    print("you have enter an invalid input:")

