from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from flask_ckeditor import CKEditor
from forms import CreateToDo



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
ckeditor=CKEditor(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)
    doing = db.Column(db.Boolean)
    done = db.Column(db.Boolean)
db.create_all()


@app.route('/', methods=['GET', 'POST'])
def home():
    form = CreateToDo()
    tasks = Task.query.all()
    if form.validate_on_submit():
        new_task = Task(
            task=form.task.data
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('index.html', form=form, tasks=tasks)


@app.route('/complete/<id>')
def complete(id):
    task = Task.query.filter_by(id=int(id)).first()
    if not task.doing:
        task.doing = True
    else:
        task.done = True
    db.session.commit()
    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)

