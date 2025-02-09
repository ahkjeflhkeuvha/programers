minNum = int(input())
maxNum = int(input())

def chk_num(num):
    if num < 2:
        return False

    if any(num%i == 0 for i in range(2, int(num**0.5) + 1)):
        return False
    else:
        return True

num_list = []
for num in range(minNum, maxNum + 1):
    if chk_num(num):
        num_list.append(num)
    
if len(num_list) == 0:
    print(-1)
else:
    sumList = sum(num_list)
    minList = min(num_list)

    print(sumList)
    print(minList)