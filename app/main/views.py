from flask import render_template,request,redirect,url_for,request,redirect,url_for
from . import main
from ..models import Todo
from .. import db




@main.route('/')
def index():
    todo_list=Todo.query.all()
  
    return render_template('index.html',todo_list=todo_list)

@main.route('/add',methods=["POST"])
def add():
    # add new item
    title = request.form.get("title")
    new_todo = Todo(taskname=title)
    db.session.add(new_todo)
    db.session.commit()
    
    return redirect(url_for("main.index"))

@main.route('/update/<int:todo_id>')
def update(todo_id):
    # update new item
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.isComplete = not todo.isComplete
    db.session.commit()
    
    return redirect(url_for("main.index"))

@main.route('/delete/<int:todo_id>')
def delete(todo_id):
    # delete item
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    
    return redirect(url_for("main.index"))



@main.route('/about')
def about():
    return render_template('about.html')
