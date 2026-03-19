first_name = str(input("Enter your firstname: "))
last_name = str(input("Enter your lastname: "))
print("Firstname is: ", first_name)
print("Lastname is: ", last_name)
age = int(input("Enter your age: "))
if age >= 18:
    print("you are eligible to vote for this election period")
else:
    print("Your age does not meet the voting requirements for this year's election")
if age >= 18:
    print("On probation")
else:
    print("access denied")

height = float(input("Please Enter your height: "))
weight = float(input("What is your Weight: "))
bmi = weight / (height ** 2)
print("Your bmi is: ", bmi)
if bmi < 18.5:
    print("you are underweight")
