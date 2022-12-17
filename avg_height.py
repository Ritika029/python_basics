# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
#print(student_heights)
summation=0 
for height in student_heights:
    summation = summation + height

number=0
for num in student_heights:
    number+=1

summation_new= round(summation/number)
print(summation_new)



