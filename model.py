from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.debug = False
app.config['SECRET_KEY'] = 'df9d9b8a053375dbae2758d00192748b77c1208ddd6e478c65b35e982c3c633b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    user_lvl = db.Column(db.Integer(), default=0)
    role = db.Column(db.String(255), nullable=False, default="user")

    tests_history = db.relationship('TestHistory', backref='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Test(db.Model):
    __tablename__ = "test"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    questions = db.relationship('Question', backref='test')
    tests_history = db.relationship('TestHistory', backref='test')


class Question(db.Model):
    __tablename__ = "question"
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    subject = db.Column(db.String(255), nullable=False)
    test_id = db.Column(db.Integer(), db.ForeignKey('test.id'))
    data_list = db.relationship('Data', backref='question')
    questions_history = db.relationship('QuestionHistory', backref='question')


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String)
    answer = db.Column(db.Integer)
    img = db.Column(db.Integer(), default=0)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))


class TestHistory(db.Model):
    __tablename__ = "test_history"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    result = db.Column(db.Integer(), default=0)
    active = db.Column(db.Boolean(), default=True)
    test_id = db.Column(db.Integer(), db.ForeignKey('test.id'))
    questions_history = db.relationship('QuestionHistory', backref='test_history')


class QuestionHistory(db.Model):
    __tablename__ = "question_history"
    id = db.Column(db.Integer(), primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    title = db.Column(db.String(255), nullable=False)
    img = db.Column(db.Integer(), nullable=False)
    data_id = db.Column(db.Integer(), db.ForeignKey('data.id'))
    subject = db.Column(db.String(255), nullable=False)
    true_answer = db.Column(db.String(255), nullable=False)
    user_answer = db.Column(db.String(255), nullable=True)
    test_history_id = db.Column(db.Integer, db.ForeignKey('test_history.id'))
    answers_list = db.relationship('Answer', backref='question_history')


class Answer(db.Model):
    __tablename__ = "answer"
    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    question_history_id = db.Column(db.Integer, db.ForeignKey('question_history.id'))


def save(obj):
    db.session.add(obj)
    db.session.commit()
