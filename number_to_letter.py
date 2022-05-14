numerical_grade = float(input("What was your score out of 100?: "))
if numerical_grade >= 90:
    letter = "A" 
elif numerical_grade >= 80: 
    letter = "B"
elif numerical_grade >= 70: 
    letter = "C"
elif numerical_grade >= 60:
    letter = "D"
else:
    letter = "F" 
print(letter)