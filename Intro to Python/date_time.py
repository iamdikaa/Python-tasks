from datetime import datetime, timedelta
today = datetime.now()
print('Today is' + ' ' + str(today))

# print("Today's date is:" + ' ' + str(today.day))
# print('This week is:' + ' ' + str(today.weekday()))
# print('The month is:' + ' ' + str(today.month))
# print('The year is:' + ' ' + str(today.year))

#another example of calculating yesterday
one_day = timedelta(weeks=1)
lastweek = today - one_day
print('Lastweek is:' + ' ' + str(lastweek))

# birthday = input('When is your birthday: (dd/mm/yyyy)?')
# birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
# print('birthday:' + str(birthday_date))