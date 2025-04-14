import heapq
import sys

T = int(input())
input()

for _ in range(T): # 테스트의 개수
    N, M = map(int, input().split())

    S_warriors = list(map(int, sys.stdin.readline().strip().split()))
    heapq.heapify(S_warriors)

    B_warriors = list(map(int, sys.stdin.readline().strip().split()))
    heapq.heapify(B_warriors)

    # print(S_warriors, B_warriors)
    
    sys.stdin.readline().strip()

    while S_warriors and B_warriors:
        if S_warriors[0] < B_warriors[0]:
            heapq.heappop(S_warriors)
        elif B_warriors[0] <= S_warriors[0]: 
            heapq.heappop(B_warriors)

    print("S" if S_warriors else "B")
        
