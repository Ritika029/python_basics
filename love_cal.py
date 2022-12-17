# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_new = name1.lower()
name2_new = name2.lower()

t_name1 = name1_new.count("t")
r_name1 = name1_new.count("r")
u_name1 = name1_new.count("u")
e_name1 = name1_new.count("e")
l_name1 = name1_new.count("l")
o_name1 = name1_new.count("o")
v_name1 = name1_new.count("v")
e_name1 = name1_new.count("e")

t_name2 = name2_new.count("t")
r_name2 = name2_new.count("r")
u_name2 = name2_new.count("u")
e_name2 = name2_new.count("e")
l_name2 = name2_new.count("l")
o_name2 = name2_new.count("o")
v_name2 = name2_new.count("v")
e_name2 = name2_new.count("e")

true_name = t_name1+t_name2+r_name1+r_name2+u_name1+u_name2+e_name1+e_name2
love_name = l_name1+l_name2+o_name1+o_name2+v_name1+v_name2+e_name1+e_name2

amount=str(true_name)+str(love_name)
amount_new =int(amount)
if amount_new<10 or amount_new>90:
    print("Your score is "+ amount+ ", you go together like coke and mentos.")
elif 40<+amount_new<=50:
    print("Your score is "+ amount+ ", you are alright together.")
else:
    print("Your score is "+ amount+ ".")