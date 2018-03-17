from operator import itemgetter

users = [
    {'fname': 'Bucky', 'lname': 'Roberts'},
    {'fname': 'Tom', 'lname': 'Roberts'},
    {'fname': 'Bernie', 'lname': 'Zunks'},
    {'fname': 'Jenna', 'lname': 'Hayes'},
    {'fname': 'Sally', 'lname': 'Jones'},
    {'fname': 'Amanda', 'lname': 'Roberts'},
    {'fname': 'Tom', 'lname': 'Willams'},
    {'fname': 'Dean', 'lname': 'Hayes'},
    {'fname': 'Bernie', 'lname': 'Barbie'},
    {'fname': 'Tom', 'lname': 'Jones'}
]

sorted_users = sorted(users, key=itemgetter('fname', 'lname'))


print(sorted_users)
print(sorted_users[0]['fname'])
#for x in sorted(users, key=itemgetter('fname', 'lname')):
 #   print(x)