x = 6
y = 9
if x > y:
    print(True)
else:
    print(False)


stanley = 'male'
favour = 'female'
if favour == 'male':
    print(False)
else:
    print(True)


print(2 == int('2'))

male = True
female = False

stanley = male
favour = female

if favour == male:
    print(True)
else:
    print(False)

#and operator
print(True and True)
print(True and False)

#or operator
print(False or True)
print(False or False)

#not operator
print(not True)
print(not False)

#mixing boolean and comparision
print((4>5) and (5<4))
print((5==5) and (6!=6))
print((2<4) or (3==4))