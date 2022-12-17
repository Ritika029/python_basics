
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name_list = names
random_namenum = random.randrange(len(name_list))
random_num = name_list[random_namenum]

print(str(random_num)+ " is going to buy the meal today!")