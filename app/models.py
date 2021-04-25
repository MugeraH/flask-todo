from . import db

#...

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer,primary_key = True)
    taskname = db.Column(db.String(255))
    isComplete = db.Column(db.Boolean,default=False, server_default="false")

    def __repr__(self):
        return f'User {self.taskname}'
