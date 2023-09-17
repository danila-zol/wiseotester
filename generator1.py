import random
import math
from recorders import add_records


# Определяем функцию shablon_1
def shablon_1(size=100):
    shablon_1 = {}
    shablon_1['text'] = 'Вычислите мощность тока, зная, что I = {i} и U = {u}'

    shablon_1['i'] = random.sample(range(1, 101), size)
    shablon_1['u'] = random.sample(range(1, 101), size)
    shablon_1['ans'] = []
    for x in range(len(shablon_1['i'])):
        shablon_1['ans'].append(shablon_1['i'][x] * shablon_1['u'][x])

    # Обновляем данные в таблице "gen"
    targarg = ['arg1;arg2' for _ in range(size)]
    targdata = ['{};{}'.format(i, u) for i, u in zip(shablon_1['i'], shablon_1['u'])]
    ans = [ans for ans in shablon_1['ans']]
    ttype = [1 for _ in range(size)]
    img = [1 for _ in range(size)]

    add_records(targdata, ans, ttype, img)


def shablon_2(size=100):
    size = 100
    shablon_2 = {}
    shablon_2[
        'text'] = 'Определите работу электродвигателя если известно, что его мощность равна {p} и время {t}(мин). Ответ предоставте в кДж(округлите до целых)'
    shablon_2['p'] = random.sample(range(1, 101), size)
    shablon_2['t'] = random.sample(range(1, 101), size)
    shablon_2['ans'] = []
    for x in range(len(shablon_2['p'])):
        shablon_2['ans'].append(round((shablon_2['p'][x] * shablon_2['t'][x] * 60) / 1000))
    targarg = ['arg1;arg2' for _ in range(size)]
    targdata = ['{};{}'.format(p, t) for p, t in zip(shablon_2['p'], shablon_2['t'])]
    ans = [ans for ans in shablon_2['ans']]
    ttype = [2 for _ in range(size)]
    img = [0 for _ in range(size)]

    add_records(targdata, ans, ttype, img)


def shablon_3(size=100):
    size = 100
    shablon_3 = {}
    shablon_3[
        'text'] = 'Определите силу тока, если в цепи протекает заряд {q} А·ч за время {t} секунд. Округлите до двух знаков после запятой'
    shablon_3['q'] = random.sample(range(10001, 10101), size)
    shablon_3['t'] = random.sample(range(1, 101), size)
    shablon_3['ans'] = []
    for x in range(len(shablon_3['q'])):
        shablon_3['ans'].append(round(shablon_3['q'][x] / (shablon_3['t'][x] * 3600), 2))
    targarg = ['arg1;arg2' for _ in range(size)]
    targdata = ['{};{}'.format(q, t) for q, t in zip(shablon_3['q'], shablon_3['t'])]
    ans = [ans for ans in shablon_3['ans']]
    ttype = [3 for _ in range(size)]
    img = [0 for _ in range(size)]

    add_records(targdata, ans, ttype, img)


def shablon_4(size=100):
    size = 100
    shablon_4 = {}
    shablon_4[
        'text'] = 'Найдите электрическое сопротивление проводника, если при напряжении {u} В на нем протекает ток {i} А. Округлите до двух знаков после запятой'
    shablon_4['u'] = random.sample(range(1, 101), size)
    shablon_4['i'] = random.sample(range(1, 101), size)
    shablon_4['ans'] = []
    for x in range(len(shablon_4['u'])):
        shablon_4['ans'].append(round(shablon_4['u'][x] / shablon_4['i'][x], 2))
    targarg = ['arg1;arg2' for _ in range(size)]
    targdata = ['{};{}'.format(u, i) for u, i in zip(shablon_4['u'], shablon_4['i'])]
    ans = [ans for ans in shablon_4['ans']]
    ttype = [4 for _ in range(size)]
    img = [1 for _ in range(size)]

    add_records(targdata, ans, ttype, img)


def shablon_5(size=100):
    size = 100
    shablon_5 = {}
    shablon_5['text'] = 'Определите напряжение на проводнике, если его сопротивление {r} Ом, а сила тока {i} А'
    shablon_5['r'] = random.sample(range(1, 101), size)
    shablon_5['i'] = random.sample(range(1, 101), size)
    shablon_5['ans'] = []
    for x in range(len(shablon_5['r'])):
        shablon_5['ans'].append(shablon_5['r'][x] * shablon_5['i'][x])
    targarg = ['arg1;arg2' for _ in range(size)]
    targdata = ['{};{}'.format(r, i) for r, i in zip(shablon_5['r'], shablon_5['i'])]
    ans = [ans for ans in shablon_5['ans']]
    ttype = [5 for _ in range(size)]
    img = [1 for _ in range(size)]

    add_records(targdata, ans, ttype, img)


def shablon_6(size=100):
    shablon_6 = {}
    shablon_6[
        'text'] = 'Сколько зарядов проходит через проводник за {t} секунд, если ток равен {i} А? Ответ разделите на 10 в 17 степени.'
    shablon_6['t'] = random.sample(range(1, 101), size)
    shablon_6['i'] = random.sample(range(1, 101), size)
    shablon_6['ans'] = []
    for x in range(len(shablon_6['t'])):
        shablon_6['ans'].append(round(shablon_6['i'][x] * shablon_6['t'][x] / (1.6 * pow(10, -19)) / pow(10, 17)))
    targarg = ['arg1;arg2' for _ in range(size)]
    targdata = ['{};{}'.format(t, i) for t, i in zip(shablon_6['t'], shablon_6['i'])]
    ans = [ans for ans in shablon_6['ans']]
    ttype = [6 for _ in range(size)]
    img = [0 for _ in range(size)]

    add_records(targdata, ans, ttype, img)


def shablon_7(size=100):
    shablon_7 = {}
    shablon_7[
        'text'] = 'Найдите сопротивление проволоки, если известно, что ее длина равна {l} м, а площадь поперечного сечения составляет {s} мм^2? Округлите до 2 знаков после запятой'
    shablon_7['l'] = random.sample(range(10001, 10101), size)
    shablon_7['s'] = random.sample(range(1, 101), size)
    shablon_7['ans'] = []
    for x in range(len(shablon_7['l'])):
        shablon_7['ans'].append(round((4 * pow(10, -3) * shablon_7['l'][x]) / shablon_7['s'][x], 2))
    targarg = ['arg1;arg2' for _ in range(size)]
    targdata = ['{};{}'.format(l, s) for l, s in zip(shablon_7['l'], shablon_7['s'])]
    ans = [ans for ans in shablon_7['ans']]
    ttype = [7 for _ in range(size)]
    img =[0 for _ in range(size)]

    add_records(targdata, ans, ttype, img)


def shablon_8(size=100):
    size = 100
    shablon_8 = {}
    shablon_8[
        'text'] = 'Определите величину силы тока, протекающего через проводник сопротивлением {r} Ом, если приложенное к нему напряжение составляет {u} В. Округлите до двух знаков после запятой'
    shablon_8['r'] = random.sample(range(1, 101), size)
    shablon_8['u'] = random.sample(range(1, 101), size)
    shablon_8['ans'] = []
    for x in range(len(shablon_8['r'])):
        shablon_8['ans'].append(round(shablon_8['u'][x] / shablon_8['r'][x], 2))
    targarg = ['arg1;arg2' for _ in range(size)]
    targdata = ['{};{}'.format(r, u) for r, u in zip(shablon_8['r'], shablon_8['u'])]
    ans = [ans for ans in shablon_8['ans']]
    ttype = [8 for _ in range(size)]
    img = [1 for _ in range(size)]

    add_records(targdata, ans, ttype, img)


# Девятый шаблон
def shablon_9(size=100):
    size = 100
    shablon_9 = {}
    shablon_9[
        'text'] = 'Определите индуктивность катушки, если частота тока {f} Гц, емкость конденсатора {c} Ф и ёмкость катушки примерно равна емкости конденсатора.Умножте на 1000 и округлите до двух знаков после запятой'
    shablon_9['f'] = random.sample(range(1, 101), size)
    shablon_9['c'] = random.sample(range(1, 101), size)
    shablon_9['ans'] = []
    for x in range(len(shablon_9['f'])):
        shablon_9['ans'].append(round(1 / (2 * math.pi * shablon_9['f'][x] * shablon_9['c'][x]) * 1000, 2))
    targarg = ['arg1;arg2' for _ in range(size)]
    targdata = ['{};{}'.format(f, c) for f, c in zip(shablon_9['f'], shablon_9['c'])]
    ans = [ans for ans in shablon_9['ans']]
    ttype = [9 for _ in range(size)]
    img = [9 for _ in range(size)]

    add_records(targdata, ans, ttype, img)


# Десятый шаблон
def shablon_10(size=100):
    size = 100
    shablon_10 = {}
    shablon_10['text'] = 'Вычислите сопротивление цепи, в которой последовательно соединены резисторы {r1} Ом и {r2} Ом'
    shablon_10['r1'] = random.sample(range(1, 101), size)
    shablon_10['r2'] = random.sample(range(1, 101), size)
    shablon_10['ans'] = []
    for x in range(len(shablon_10['r1'])):
        shablon_10['ans'].append(shablon_10['r1'][x] + shablon_10['r2'][x])
    targarg = ['arg1;arg2' for _ in range(size)]
    targdata = ['{};{}'.format(r1, r2) for r1, r2 in zip(shablon_10['r1'], shablon_10['r2'])]
    ans = [ans for ans in shablon_10['ans']]
    ttype = [10 for _ in range(size)]
    img = [10 for _ in range(size)]

    add_records(targdata, ans, ttype, img)
