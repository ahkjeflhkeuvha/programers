# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error

line = []
for i in range(3):
    line.append(int(input()))

line.sort()
s = sum(line)

if s != 180:
    print("Error")
else:
    if line[0] == line[2]:
        print("Equilateral")
    elif line[0] == line[1] or line[1] == line[2]:
        print("Isosceles")
    else:
        print("Scalene")