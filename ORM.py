from orm import Model , StringField , InterField

class User(Model):
    __table__='users'

    id = InterField(primary_key=True)
    name= StringField()

user=User(id = 123,name='username')
user.insert()
users= User.findAll()

