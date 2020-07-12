from book.models import Book
from django.contrib.auth.models import User

# INSERTS USERS
csv_file=open("final.txt").readlines()
for i in csv_file[1:]:
    try:
        username=''.join(i.split())
        print(username)
        user = User(username = username, password=username)
        user.save()
    except:
        pass
# INSERTS BOOKS
for i in csv_file[1:]:
    cols = i.split(';')
    try:
    	username=''.join(cols[2][1:-1].split())
    	image_url = cols[7].split('"')[1]
    	book = Book(name = cols[1][1:-1],isbn13=cols[0][1:-1],author = User.objects.get(username= username),published_year= cols[3][1:-1],publisher = cols[4][1:-1],image=image_url)
    	book.save()	
    except:
    	pass
