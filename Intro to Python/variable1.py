message = 'Welcome to python'
print(message)

message = 'Hope you are enjoying it?'
print(message)

message = 'Great to have you here stan'
print(message)

message = "It's what it is"
print(message)

first_name = 'sarah'
last_name = 'jane'
full_name = first_name + ' '+ last_name
print(full_name)

first_name = 'vision'
last_name = 'lewis'
full_name = first_name + ' ' + last_name
print('Hello' + ' ' + first_name + ' ' + last_name)

first_name = input('What is your first name?')
last_name = input('What is your last name?')
full_name = first_name + ' ' + last_name
print('Hello' + ' '+ first_name.capitalize() + ' ' + last_name.capitalize() +'\nNice to see you' ' '+ first_name.capitalize())

#using f-string for concartenation
first_name = input('What is your first name?')
last_name = input('What is your last name?')
full_name = f"{first_name} {last_name}"
print(full_name)

#another example using f-strings
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
full_name = f'{first_name} {last_name}'
print(f"Hello, {first_name} {last_name} \nWelcome to Macquarie University, {first_name}")

