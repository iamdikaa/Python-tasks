# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#To find the minimum, you have to find the maximum first

max_score = 0

for highscore in student_scores:
    if highscore > max_score:
        max_score  = highscore
#print(f'The Maximum score is: {max_score}')


min_score = highscore

for minimum_score in student_scores:
    if minimum_score < min_score:
        min_score = minimum_score
print(f'The Minimum Score is: {min_score}') 