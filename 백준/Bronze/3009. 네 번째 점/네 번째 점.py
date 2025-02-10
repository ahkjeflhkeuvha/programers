x_dic = {}
y_dic = {}


for i in range(3):
    x, y = map(int, input().split())
   
    if x not in x_dic:
        x_dic[x] = 1
    else:
        x_dic[x] += 1

    if y not in y_dic:
        y_dic[y] = 1
    else:
        y_dic[y] += 1

for key in x_dic.keys():
    if x_dic[key] == 1:
        print(key, end = " ")

for key in y_dic.keys():
    if y_dic[key] == 1:
        print(key, end="")