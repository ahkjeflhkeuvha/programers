N = int(input())

case_arr = [1, 1, 2]

while len(case_arr) <= N:
    case_arr.append((case_arr[-1] + case_arr[-2]) % 10007)

print(case_arr[N])
