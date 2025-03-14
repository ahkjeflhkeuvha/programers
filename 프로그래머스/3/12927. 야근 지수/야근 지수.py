import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0

    works = [-w for w in works]
    heapq.heapify(works)

    while n > 0:
        max_work = -heapq.heappop(works)
        if max_work == 0:
            break
        max_work -= 1
        heapq.heappush(works, -max_work)
        n -= 1

    return sum(w**2 for w in works)
