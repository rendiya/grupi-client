from werkzeug.security import generate_password_hash, check_password_hash
print "abs"
class User(object):

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

me = generate_password_hash('defaultx')
#me = 'pbkdf2:sha1:1000$lEyXGiyv$eb22fdff198fe42e6db293dba18cebcf98704da2'
print me
#print me.check_password(me,'default')
print check_password_hash(me, 'defaultx')
#print me.check_password('John Doe')
