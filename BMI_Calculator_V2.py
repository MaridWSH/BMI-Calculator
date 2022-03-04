weight = int( input("enter your Weight in kg : ") )
height = float( input("enter your Hight in m : ") )
BMI =  (round(weight / (height **2 ))) 
print (f"Your Body Mass Index is : {BMI} kg/m2" )

if BMI <= 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif 18.5 < BMI <= 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif 25 < BMI <= 30:
    print(f"Your BMI is {BMI}, you have a normal  slightly overweight.")
elif 30 < BMI <= 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")

print(input("Press Enter To Exit."))
