grade = input() 

grade_dic = {
    'A' : 4.0,
    'B' : 3.0,
    'C' : 2.0,
    'D' : 1.0,
    'F' : 0.0
}

case_dic = {
    '+' : 0.3,
    '0' : 0.0,
    '-' : -0.3,
    '' : 0.0
}

print(grade_dic[grade[0]] + case_dic[grade[1]] if len(grade) > 1 else 0.0)