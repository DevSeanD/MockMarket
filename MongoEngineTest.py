"""
Author: Sean Dever
Date: 2/23/2021
Description: A example database insert performed using MongoEngine Python. MongoEngine allows for class methods to be used with mongodb.
"""
import datetime
from mongoengine import *

connect('mongoengine_test',host='localhost',port=27017)

class Post(Document):
    title = StringField(required=True,max_length=200)
    content = StringField(required=True)
    author = StringField(required=True,max_length=50)
    published = DateTimeField(default=datetime.datetime.now)

post0 = Post(
        title='First Post',
        content='Content example',
        author='Sean'
        )

post0.save()
print(post0.title)
post0.title = 'A Better Post Title'
post0.save()
print(post0.title)

