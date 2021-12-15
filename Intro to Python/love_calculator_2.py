#Love calculator


print('''
                .---.   .---.
              ,';'   `.';'   `..
              f               :Bo.
              `               d88:
               `\           /d88P'
                 `\     ; /d888P'
                   `.  ',d8&8P'
                     : ;d8&7'
                      | :8:
                         |  qx
''')

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


combined_string = name1 + name2
lower_case = combined_string.lower()

t1 = combined_string.count('t') 
t2 = combined_string.count('r') 
t3 = combined_string.count('u') 
t4 = combined_string.count('e') 

print(f'T occurs {t1} times')
print(f'R occurs {t2} times')
print(f'U occurs {t3} times')
print(f'E occurs {t4} times')
total1 = str(t1 + t2 + t3 + t4)
print('Total =' + ' ' +total1)

t5 = combined_string.count('l')
t6 = combined_string.count('o')
t7 = combined_string.count('v')
t8 = combined_string.count('e')

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