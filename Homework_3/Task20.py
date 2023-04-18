score_dict ={'AEIOULNSTRАВЕИНОРСТ':1, 'DGДКЛМПУ':2, 'BCMPБГЁЬЯ':3, 'FHVWYЙЫ':4, 'KЖЗХЦЧ':5, 'JXШЭЮ':8, 'QZФЩЪ':10}
word = input('Введите слово - ').upper()
score = 0
for n in word:
    for i in score_dict.keys():
        if n in i:
            score += score_dict[i]
print (f"Счет - {score}")
