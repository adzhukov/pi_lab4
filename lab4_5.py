import pymorphy2

from sys import argv

morph = pymorphy2.MorphAnalyzer()

numbers = {
    'один': 1,
    'два': 2,
    'три': 3,
    'четыре': 4,
    'пять': 5,
    'шесть': 6,
    'семь': 7,
    'восемь': 8,
    'девять': 9,

    'одиннадцать': 11,
    'двенадцать': 12,
    'тринадцать': 13,
    'четырнадцать': 14,
    'пятнадцать': 15,
    'шестнадцать': 16,
    'семнадцать': 17,
    'восемнадцать': 18,
    'девятнадцать': 19,

    'десять': 10,
    'двадцать': 20,
    'тридцать': 30,
    'сорок': 40,
    'пятьдесят': 50,
    'шестьдесят': 60,
    'семьдесят': 70,
    'восемьдесят': 80,
    'девяносто': 90,

    'сто': 100,
    'двести': 200,
    'триста': 300,
    'четыреста': 400,
    'пятьсот': 500,
    'шестьсот': 600,
    'семьсот': 700,
    'восемьсот': 800,
    'девятьсот': 900,
}

scale = {
    'тысяча': 10**3,
    'миллион': 10**6,
    'миллиард': 10**9,
    'триллион': 10**12,
    'квадриллион': 10**15,
    'квинтиллион': 10**18,
    'секстиллион': 10**21,
    'септиллион': 10**24,
    'октиллион': 10**27,
    'нониллион': 10**30,
    'дециллион': 10**33,
    'ундециллион': 10**36,
    'дуодециллион': 10**39,
    'тредециллион': 10**42,
}


filename = argv[-1]

with open(filename, 'r') as f:
    text = f.read()

words = text.split()
modified_text = []
result = 0
temp = 0
for word in words:
    normal_form = morph.parse(word)[-1].normal_form
    if normal_form in numbers:
        temp += numbers[normal_form]
    elif normal_form in scale:
        if not temp:
            temp = 1
        temp *= scale[normal_form]
        result += temp
        temp = 0
    else:
        if temp:
            result += temp
            modified_text += [str(result)]
            result = 0
        temp = 0
        modified_text += [word]

if temp:
    modified_text += [str(result + temp)]

modified_text = ' '.join(modified_text)
print(modified_text)
