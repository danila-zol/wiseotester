import random
from random import randint

from flask import render_template, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from generator import deter_gen_2, deter_gen_3, cosine_theorem_gen, square_equasion_gen, \
    triangle_S_gen, simple_sum_equation_gen, simple_sub_equation_gen, simple_mult_equation_gen, simple_div_equation_gen
from generator1 import shablon_1, shablon_2, shablon_3, shablon_4, shablon_5, shablon_6, shablon_7, shablon_8, \
    shablon_9, shablon_10
from model import db, app, User, Test, Question, Data, QuestionHistory, TestHistory, save, Answer
from recorders import create_reference_table

login_manager = LoginManager(app)
login_manager.login_view = '/'


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


@app.route('/show_test_result/<test_history_id>', methods=['POST', 'GET'])
@login_required
def show_test_result(test_history_id):
    test_history = db.session.query(TestHistory).filter(
        TestHistory.id == test_history_id).first()
    test_history.active = False
    save(test_history)
    questions_test_history = db.session.query(QuestionHistory).filter(
        QuestionHistory.test_history_id == test_history_id).all()
    test_result = test_history.result / len(test_history.questions_history)
    return render_template('test_result.html', test_history=test_history, test_result=test_result,
                           message=f"{test_history.result}/{len(test_history.questions_history)}, "
                                   f"{round(test_result * 100, 2)}%", questions_test_history=questions_test_history)


def get_current_user_active_test_history():
    for test_history in current_user.tests_history:
        if test_history.active is True:
            return test_history


@app.get('/show_test/<test_id>')
@login_required
def show_test(test_id):
    test = db.session.query(Test).filter(
        Test.id == test_id).first()

    active_test_history = get_current_user_active_test_history()

    if active_test_history is None:
        active_test_history = TestHistory(name=test.name, user_id=current_user.id, active=True, test_id=test_id)

        for question in test.questions:
            question_after_change = question_change(question.title, question.id)
            question_history = QuestionHistory(question_id=question.id, true_answer=question_after_change[4],
                                               title=question_after_change[0], img=question_after_change[2],
                                               data_id=question_after_change[3],
                                               subject=question.subject,
                                               test_history_id=active_test_history.id)
            active_test_history.questions_history.append(question_history)
            for i in question_after_change[1]:
                question_history.answers_list.append(Answer(text=i))

        save(active_test_history)
    return next_question()


@app.route('/next_question', methods=['POST', 'GET'])
@login_required
def next_question():
    question_history_id = request.form.get("question_history_id")
    answer = request.form.get("answer")
    active_test_history = get_current_user_active_test_history()

    if answer is not None:
        answer = answer.replace("(", "")
        answer = answer.replace(")", "")
        answer = answer.replace("'", "")
        answer = answer.split(",")
        answer = [int(i) for i in answer]
        data = db.session.query(Data).filter(
            Data.id == answer[1]).first()
        if answer[0] == data.answer:
            active_test_history.result += 1
            save(active_test_history)

        question_history = db.session.query(QuestionHistory).filter(
            QuestionHistory.id == question_history_id).first()
        if question_history.user_answer is None:
            question_history.user_answer = str(answer[0])
        save(question_history)

    questions_history = active_test_history.questions_history
    for question_history in questions_history:
        if question_history.user_answer is None:
            return show_test_question(question_history.id)

    return show_test_result(active_test_history.id)


@app.get('/show_test_question/<question_history_id>')
@login_required
def show_test_question(question_history_id):
    question_history = db.session.query(QuestionHistory).filter(QuestionHistory.id == question_history_id).first()
    return render_template('question.html', question_history=question_history, question_title=question_history.title,
                           answers=question_history.answers_list,
                           img=question_history.img, id_data=question_history.data_id)


def question_change(title, question_id):
    data = db.session.query(Data).filter(
        Data.question_id == question_id).all()
    data = random.choice(data)
    count = data.data.split(";")
    answers = [round(data.answer)]
    for i in range(3):
        temp2 = data.answer
        if temp2 < 0:
            temp2 = temp2 * (-1)
        answers.append(randint(1, round(temp2) + 10))
    random.shuffle(answers)
    temp = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    new_title = ""
    for i in title:
        if i in temp:
            new_title += str(count[int(i)])
        else:
            new_title += i
    return new_title, answers, data.img, data.id, data.answer


@app.get('/profile')
@login_required
def show_profile():
    tests = db.session.query(TestHistory.user_id == current_user.id).all()
    all_result = 0
    # print(tests)
    # if len(tests) != 0:
    #     for i in tests:
    #         all_result += i.result
    #     all_result = all_result / len(tests)
    return render_template('profile.html', user=current_user,tests=len(tests))


@app.get('/logout')
@login_required
def logout():
    logout_user()
    return render_template('login.html')


@app.get('/tests')
@login_required
def show_tests_page():
    tests = db.session.query(Test).all()
    return render_template('tests.html', tests=tests)


@app.get("/admin")
@login_required
def show_admin_panel(message=""):
    if current_user.role == "admin":
        tests = db.session.query(Test).all()
        return render_template("admin.html", tests_list=tests, message=message)
    else:
        return index(message="Вы не авторизованы")


@app.get('/educate')
@login_required
def show_educate_page():
    return render_template('educate.html')


@app.route('/')
def index(message=None):
    if current_user.is_authenticated:
        return show_profile()
    else:
        return render_template('login.html', message=message)


@app.post('/registration')
def registration():
    user = User(username=request.form.get("username"), name=request.form.get("name"),
                email=request.form.get("email"))
    user.set_password(request.form.get("password"))
    save(user)
    return index()


@app.post('/login')
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    user = db.session.query(User).filter(User.username == username).first()
    if user and user.check_password(password):
        login_user(user, remember=True)
        return show_profile()
    else:
        return show_login_form(message="Ошибка авторизации")


@app.get('/login')
def show_login_form(message=None):
    return render_template("login.html", message=message)


@app.get('/registration')
def show_registration_form(message=None):
    return render_template("registration.html", message=message)


def insert_admin():
    if db.session.query(User).filter(User.username == "admin").first() is None:
        user = User(username="admin", name="admin",
                    email="admin", role="admin")
        user.set_password("admin")
        save(user)


def create_test():
    tests = db.session.query(Test).all()
    if len(tests) == 0:
        test_math = Test(name="Математика")
        save(test_math)
        test_physics = Test(name="Физика")
        save(test_physics)


def main():
    app.app_context().push()
    db.create_all()
    insert_admin()
    create_reference_table()
    create_test()
    shablon_1()
    shablon_2()
    shablon_3()
    shablon_4()
    shablon_5()
    shablon_6()
    shablon_7()
    shablon_8()
    shablon_9()
    shablon_10()
    deter_gen_2()
    deter_gen_3()
    cosine_theorem_gen()
    square_equasion_gen()
    triangle_S_gen()
    simple_sum_equation_gen()
    simple_sub_equation_gen()
    simple_mult_equation_gen()
    simple_div_equation_gen()
    app.run()


if __name__ == '__main__':
    main()
