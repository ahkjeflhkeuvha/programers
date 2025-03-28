N, A, B = map(int, input().split())

if N <= B: # 지하철을 탈 수 있는 경우
    if B == A: # 둘 다 탈 수 있는 경우
        print("Anything")
    elif B > A: # 버스 타는 게 더 빠른 경우
        print("Bus")
    else:
        print("Subway")

else:
    print("Bus")
