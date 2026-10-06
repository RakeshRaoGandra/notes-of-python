"""Enter your name: Rakesh
Enter your age: 20
Enter your exam score: 85
Enter total marks: 100

Student Name: Rakesh
Age: 20
Score: 85
Total Marks: 100
Percentage: 85.0

Score greater than 50: True
Score greater than or equal to 75: True
Score less than 40: False
Score less than or equal to 100: True
Score exactly 85: True


"""

name=input("Enter your name : ")
age=int(input("enter your age :"))
Score=int(input("enter your score :"))
totalmarks=int(input("enter your marks :"))

print("Student Name :",name)

print(Score>50)
#percentage = (score / total_marks) * 100