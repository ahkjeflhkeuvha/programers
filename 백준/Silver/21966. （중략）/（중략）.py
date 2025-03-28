N = int(input())
S = input()

# S의 길이가 25 이하면 S를 그대로 출력한다.
if N <= 25:
    print(S)
else:
    middle_part = S[11:-11]  # 중간 부분 추출
    if '.' not in middle_part or (middle_part[-1] == "." and middle_part.count(".") == 1): # 한 문장인 경우 마지막이 .이거나 .이 없는 경우
        print(S[:11] + "..." + S[-11:])
    else:
        print(S[:9] + "......" + S[-10:])
