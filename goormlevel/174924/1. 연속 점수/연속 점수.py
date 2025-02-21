# -*- coding: utf-8 -*-
# UTF-8 encoding when using Korean
N = int(input())
scores = list(map(int, input().split()))

case1 = max(scores)
case2 = 0 

temp_sum = scores[0] 
max_consecutive = temp_sum 

for i in range(1, N):
    if scores[i] - scores[i - 1] == 1:
        temp_sum += scores[i]
    else:
        max_consecutive = max(max_consecutive, temp_sum) 
        temp_sum = scores[i]  

max_consecutive = max(max_consecutive, temp_sum)

print(max(case1, max_consecutive))
