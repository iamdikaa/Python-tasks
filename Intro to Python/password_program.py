name = input('What is your name?')
password = input('What is your password?')
age = input('What is your age?')

# if name == 'stanley':
#     print('Hello stanley')
#     if password == 'dikachi':
#         print('Access Granted')
# else:
#             print('Access denied')


# if name == 'stanley':
#     print('Hello stanley')
# elif int(age) < 25:
#     print('Hi, Stranger, you are not the user, kiddo')
# elif age > 25:
#     print('You are not the user')

if name == 'stanley':
    print('Hello, Stanley')
elif int(age) < 18:
    print('Hey Kiddo, you arent the users')
elif int(age) > 30:
    print('The user is not this old')
elif int(age) > 60:
    print('Hey oldie, the user is not this old')
else:
    print('you are neither a kid nor an oldie, get out')