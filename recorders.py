from model import Question, Data, app, db


def parse_array(arr):
    tmp = ""
    for i in arr:
        tmp += str(i) + ";"
    return tmp[:-1]


def parse_arr_string(string):
    tmp = []
    for i in string.split(";"):
        tmp.append(int(i))
    return tmp


def add_record(tdata, tans, ttype, img):
    # generate the record
    record = Data(data=parse_array(tdata), answer=tans, question_id=ttype, img=img)

    # commit the record
    with app.app_context():
        db.session.add(record)
        db.session.commit()


def add_records(targdata, ans, ttype, img):
    for targd, anse, type, imgs in zip(targdata, ans, ttype, img):
        record = Data(data=targd, answer=anse, question_id=type, img=imgs)
        with app.app_context():
            db.session.add(record)
            db.session.commit()


def add_text_record(ttext, tsubject, test_id):
    record = Question(title=ttext, subject=tsubject, test_id=test_id)
    db.session.add(record)
    db.session.commit()


def create_reference_table():
    # generate physics refrence
    with open("physics_templates", "r", encoding="utf-8") as f:
        for i in f.readlines():
            add_text_record(i, "physics", 2)
        f.close()

    # generate math refrence
    with open("Сustom/math_templates", "r", encoding="utf-8") as f:
        for i in f.readlines():
            add_text_record(i, "math", 1)
        f.close()
