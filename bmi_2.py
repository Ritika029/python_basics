# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_new = height**2
bmi = weight/height_new
bmi_new = round(bmi)
bmi_word = str(bmi_new)
if bmi_new<18.5:
    print("Your BMI is "+ bmi_word+ ", you are underweight.")
elif 18.5<=bmi_new<25:
    print("Your BMI is "+ bmi_word+ ", you have a normal weight.")
elif 25<=bmi_new<30:
    print("Your BMI is "+ bmi_word+ ", you are slightly overweight.")
elif 30<=bmi_new<35:
    print("Your BMI is "+ bmi_word+ ", you are obese.")
else:
    print("Your BMI is "+ bmi_word+ ", you are clinically obese.")