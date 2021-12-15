print('Hello World') #printing a hello world program

message = 'How is the night going?, stan? '
print(message)


#changing case in string with methods
name = 'stanley onyedika epuna'
print(name.title())

#changing case to upper and lower
name = 'jennifer obi'
print(name.upper())
print(name.lower())

#using variables in strings
first_name = 'stanley'
last_name = 'epuna'
full_name = f"{first_name} {last_name}"
print(full_name)

#another example from above
first_name = 'jennifer'
last_name = 'obi'
full_name = f"{first_name} {last_name}"
print(f"Hi, {full_name.title()}!")

#another example above
first_name = 'john'
last_name = 'doe'
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}"
print(message)

#Adding whitespaces to stings with Tabs or Newliines
print('Languages:\tPython')  #tabs
print('Languages:\nPython\nC\nJavaScript') #newline
print('Languages:\n\tPython\n\tC\n\tJavaScript') #combining newline and tab

#striping whitespaces
favourite_language = 'python '
print(favourite_language.rstrip())  #removing the right whitespaces

favourite_language = ' python'
print(favourite_language.lstrip()) #removing the left whitspaces

favourite_language = ' python '
print(favourite_language.strip()) #removing both left and right whitespaces
