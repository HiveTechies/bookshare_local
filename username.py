from book.models import Book
from django.contrib.auth.models import User
import csv
# INSERTS USERS
original=open('final.txt','a')
csv_file=open("authors.txt").readlines()
users=[]
for i in csv_file[1:]:
    try:
        username=''.join(i.split())
        users.append(username)
    except:
        pass
users=set(users)
users=list(users)
users.sort()
for user in users:
    original.write(user+'\n')

with open('final.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(users)