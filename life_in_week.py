# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
a = 365*90
b = 52*90
c = 12*90
age_new = int(age)
x = age_new*365
y = age_new*52
z = age_new*12
days = a-x
weeks = b-y
months = c-z
print(f"You have {days} days, {weeks} weeks, and {months} months left.")