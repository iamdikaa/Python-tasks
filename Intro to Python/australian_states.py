#Australia Catch phrases
print('''
                   _             _ _       
                | |           | (_)      
  __ _ _   _ ___| |_ _ __ __ _| |_  __ _ 
 / _` | | | / __| __| '__/ _` | | |/ _` |
| (_| | |_| \__ \ |_| | | (_| | | | (_| |
 \__,_|\__,_|___/\__|_|  \__,_|_|_|\__,_|
''')

states_in_australia = ["New South Wales", "Queensland", "South Australia", "Tasmania", "Victoria", "Western Australia", "Australian Capital Territory", "Northern Territory"]

print('Which state are you looking at?\n')
known_for = input()

if known_for == states_in_australia[0]:
    print(f'This is commonly known as: The Premier State')
    print(f'The capital city is Sydney\nIts current population is 8,172,505\nThe Premier is Gladys Berejiklian')
elif known_for == states_in_australia[1]:
    print(f'This is commonly known as: The Sunshine State')
    print(f'The capital city is Brisbane\nIts current population is 5,194,879\nThe Premier is Annastacia Palaszczuk')
elif known_for == states_in_australia[2]:
    print(f'This is commonly known as: The Festival State')
    print(f'The capital city is Adelaide\nIts current population is 1,770,790\nThe premier is Steven Marshall')
elif known_for == states_in_australia[3]:
    print(f'This is commonly known as: The Apple Isle')
    print(f'The capital city is Hobart\nThe current population is 541,506\nThe premier is Peter Gutwein')
elif known_for == states_in_australia[4]:
    print(f'This is commonly known as: The Garden State')
    print(f'The capital city is Melbourne\nThe current population is 6,661,736\nThe Premier is Daniel Andrews')
elif known_for == states_in_australia[5]:
    print(f'This is commonly known as: The Wildflower State')
    print(f'The capital city is Perth\nThe current population is 2,670,241\nThe Premier is Mark McGowan')
elif known_for == states_in_australia[6]:
    print(f'This is commonly known as: The Capital')
    print(f'The capital is Canberra\nThe current population is 431,484\nThe Chief Minister is Andrew Barr')
elif known_for == states_in_australia[7]:
    print(f'This is commonly known as: The Territory')
    print(f'The capital is Darwin\nThe current population is 246,561\nThe Chief Minister is Michael Gunner')