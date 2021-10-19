#!/usr/bin/python3

grade = eval(input("Enter grade:"))
if grade > 100 or (grade < 0) :
    print("Enter a valid grade between 0 and 100")
elif grade >= 90:
    print("Grade is 'A'")
elif grade >= 80:
    print("Grade is 'B'")
elif grade >= 70:
    print("Grade is 'C'")
elif grade >= 60:
    print("Grade is 'D'")
else:
    print("You failed")