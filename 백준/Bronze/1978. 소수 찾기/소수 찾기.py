n = int(input())
num_list = list(map(int, input().split()))

def chk_num(num):
    if num < 2:
        return False
    flag = True
    if any(num%i == 0 for i in range(2, int(num**0.5) + 1)):
        return False
    else:
        return True

answer = 0
for num in num_list:
    if chk_num(num):
        answer += 1

print(answer)