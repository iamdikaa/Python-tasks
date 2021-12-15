# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total = 0
for all_students in student_heights:
  total = total + all_students
#print(total)

total_length = 0
for avg_students in student_heights:
  total_length = total_length + 1
#print(total_length)

print(round(total / total_length))