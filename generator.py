from random import randint, shuffle, choice
import math
import json
from recorders import add_record
from model import db, app
from img_gen import *

def get_angle(point_1, point_2):
    # These can also be four parameters instead of two arrays
    angle = math.atan2(point_1[1] - point_2[1], point_1[0] - point_2[0])

    angle = math.degrees(angle)

    return angle


def find_length(point):
    return math.sqrt(point[0] ** 2 + point[1] ** 2)


def simple_div_equation_gen(SIZE=100):
    # argument names: arg, quotient
    # an equasion of the type "NUM1/x=NUM2"
    res = {"raw_data": [], "calc": 0}
    for i in range(SIZE):
        tmp = choice([2, 3, 4, 6, 12])
        tmp2 = randint(1, 20)
        res["raw_data"] = [tmp2 * tmp, tmp2]
        res["calc"] = tmp

        img_name=str(i)
        if len(img_name)<2:
            img_name="0"+img_name
        img_name="19"+img_name
        
        gen_simple_eq_img(res["raw_data"], "/", "static/img/{a}".format(a=img_name))
        
        add_record(res["raw_data"], round(res['calc']), 19, int(img_name))


def simple_mult_equation_gen(SIZE=100):
    # argument names: arg, factum
    # an equasion of the type "x*NUM1=NUM2"
    res = {"raw_data": [], "calc": 0}
    for i in range(SIZE):
        res["raw_data"] = [randint(1, 10)]
        res["raw_data"].append(res["raw_data"][0] * randint(1, 20))
        res["calc"] = res["raw_data"][1] // res["raw_data"][0]

        img_name=str(i)
        if len(img_name)<2:
            img_name="0"+img_name
        img_name="18"+img_name
        
        gen_simple_eq_img(res["raw_data"], "*", "static/img/{a}".format(a=img_name))
        
        add_record(res["raw_data"], round(res['calc']), 18, int(img_name))


def simple_sub_equation_gen(SIZE=100):
    # argument names: arg, difference
    # an equasion of the type "x-NUM1=NUM2"
    res = {"raw_data": [], "calc": 0}
    for i in range(SIZE):
        res["raw_data"] = [randint(10, 50), randint(1, 20)]
        res["calc"] = res["raw_data"][1] + res["raw_data"][0]

        img_name=str(i)
        if len(img_name)<2:
            img_name="0"+img_name
        img_name="17"+img_name

        gen_simple_eq_img(res["raw_data"], "-", "static/img/{a}".format(a=img_name))

        add_record(res["raw_data"], round(res['calc']), 17, int(img_name))


def simple_sum_equation_gen(SIZE=100):
    # argument names: arg, sum
    # an equasion of the type "x+NUM1=NUM2"
    res = {"raw_data": [], "calc": 0}
    for i in range(SIZE):
        res["raw_data"] = [randint(1, 20), randint(10, 50)]
        res["calc"] = res["raw_data"][1] - res["raw_data"][0]

        img_name=str(i)
        if len(img_name)<2:
            img_name="0"+img_name
        img_name="16"+img_name

        gen_simple_eq_img(res["raw_data"], "+", "static/img/{a}".format(a=img_name))
        add_record(res["raw_data"], round(res['calc']), 16, int(img_name))


def triangle_S_gen(SIZE=100):
    # argument names: catet1, catet2, hypotenuse
    # generates a rectangular triangle task
    res = {"raw_data": [], "calc": []}
    for i in range(SIZE):
        res["raw_data"] = [randint(1, 20), randint(1, 20)]
        res["raw_data"].append(round(math.sqrt(res["raw_data"][0] ** 2 + res["raw_data"][1])))
        res["calc"] = res["raw_data"][0] * res["raw_data"][1] / 2
        add_record(res["raw_data"], round(res['calc']), 15, 1500)


def square_equasion_gen(SIZE=100):
    # argument names: arg1..arg3
    # note: this function only generates equasions with one or zero possible roots bc we can't store arrays in the "answer" field in our DB
    res = {"raw_data": [], "calc": []}
    for i in range(SIZE):
        # flag = True
        # while flag:
        res["raw_data"] = [randint(1, 30), randint(1, 30), randint(1, 30)]
        D = res["raw_data"][1] ** 2 - res["raw_data"][0] * res["raw_data"][2] * 4
        if D < 0:
            res["calc"] = 0
            img_name=str(i)
            if len(img_name)<2:
                img_name="0"+img_name
            img_name="14"+img_name
            add_record(res["raw_data"], round(res['calc']), 14, int(img_name))
            gen_square_eq_img(res["raw_data"], "static/img/{a}".format(a=str(img_name)))
        elif D == 0:
            res["calc"] = -res["raw_data"][1] / 2 * res["raw_data"][0]
            img_name=str(i)
            if len(img_name)<2:
                img_name="0"+img_name
            img_name="14"+img_name
            add_record(res["raw_data"], round(res['calc']), 14, int(img_name))
            gen_square_eq_img(res["raw_data"], "static/img/{a}".format(a=str(img_name)))
        else:
            # continue
            pass


def cosine_theorem_gen(SIZE=100):
    # argument names: side1, side2, angle
    # "raw_data" contains two triangle sides and an angle between them
    res = {"raw_data": [], "calc": []}
    for i in range(SIZE):
        res['raw_data'] = [randint(5, 30), randint(5, 30), randint(10, 75)]
        res["calc"] = res["raw_data"][0] ** 2 + res["raw_data"][1] ** 2 - \
                      2 * res["raw_data"][0] * res["raw_data"][1] * math.cos(res["raw_data"][2])
        add_record(res["raw_data"], round(res['calc']), 13, 1300)


def deter_gen_3(SIZE=100):
    # argument names: arg1..arg9
    res = {"raw_data": 0, "calc": 0}
    for i in range(SIZE):
        res["raw_data"] = []
        for j in range(9):
            res["raw_data"].append(randint(1, 10))
        res["calc"] = (res["raw_data"][0] * res["raw_data"][4] * res["raw_data"][8] + res["raw_data"][1] *
                       res["raw_data"][5] * res["raw_data"][6] + res["raw_data"][2] * res["raw_data"][3] *
                       res["raw_data"][7]) - (
                              res["raw_data"][0] * res["raw_data"][5] * res["raw_data"][7] + res["raw_data"][1] *
                              res["raw_data"][3] * res["raw_data"][8] + res["raw_data"][2] * res["raw_data"][4] *
                              res["raw_data"][6])

        # image ID calculation
        img_name=str(i)
        if len(img_name)<2:
            img_name="0"+img_name
        img_name="12"+img_name
        
        # image and it's ID saving 
        add_record(res["raw_data"], round(res["calc"]), 12, int(img_name))
        gen_matrix_img([res["raw_data"][0:3],res["raw_data"][3:6],res["raw_data"][6:9]],"static/img/{a}".format(a=str(img_name)))


def deter_gen_2(SIZE=100):
    # argument names: arg1..arg4
    res = {"raw_data": 0, "calc": 0}
    for i in range(SIZE):
        res["raw_data"] = []
        for j in range(4):
            res["raw_data"].append(randint(1, 10))
        res["calc"] = res["raw_data"][0] * res["raw_data"][3] - res["raw_data"][1] * res["raw_data"][2]

        # image ID calculation
        img_name=str(i)
        if len(img_name)<2:
            img_name="0"+img_name
        img_name="11"+img_name
        
        # image and it's ID saving 
        add_record(res["raw_data"], round(res["calc"]), 11, int(img_name))
        gen_matrix_img([res["raw_data"][0:2],res["raw_data"][2:4]],"static/img/{a}".format(a=str(img_name)))


#app.app_context().push()
#db.create_all()

# deter_gen_2()
# deter_gen_3()
# cosine_theorem_gen()
# square_equasion_gen()
# triangle_S_gen()
#simple_sum_equation_gen(10)
#simple_sub_equation_gen(10)
#simple_mult_equation_gen(10)
#simple_div_equation_gen(10)