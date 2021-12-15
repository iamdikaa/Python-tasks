#Love calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


name1 = name1.lower()
name2 = name2.lower()

t1 = name1.count('t') and name2.count('t')
t2 = name1.count('r') and name2.count('r')
t3 = name1.count('u') and name2.count('u')
t4 = name1.count('e') and name2.count('e')

print(f'T occurs {t1} times')
print(f'R occurs {t2} times')
print(f'U occurs {t3} times')
print(f'E occurs {t4} times')
total1 = str(t1 + t2 + t3 + t4)
print('Total =' + ' ' +total1)

t5 = name1.count('l') and name2.count('l')
t6 = name1.count('o') and name2.count('o')
t7 = name1.count('v') and name2.count('v')
t8 = name1.count('e') and name2.count('e')

print(f'L occurs {t5} times')
print(f'O occurs {t6} times')
print(f'V occurs {t7} times')
print(f'E occurs {t8} times')
total2 = str(t5 + t6 + t7 + t8)
print('Total =' + ' ' +total2)

love_score = total1 + total2
print(f'Your score is {love_score}%')

love_score = int(love_score)

if love_score < 10 or love_score > 90:
  print(f'Your score is {love_score}, you go together like coke and mentos')
elif love_score >=40 and love_score <=50:
  print(f'Your score is {love_score}, you are alright together')
else:
  print(f'Your score is {love_score}')