# 1/1
# 1/2 2/1
# 3/1 2/2 1/3
# 1/4, 2/3, 3/2, 4/1

num = int(input())
line = 1

while num > line:
    num -= line
    line += 1
    
if line%2 == 0: # 짝수 번째는 1/n부터 시작
    print('{}/{}'.format(num, line-num+1))
else: # 홀수 번째는 n/1부터 시작
    print('{}/{}'.format(line-num+1, num))
