N, M = map(int, input().split())
woods = list(map(int, input().split()))

start = 0
end = max(woods)

while start <= end:
    mid = (start + end) // 2
    diff = 0

    for wood in woods:
        if wood >= mid:
            diff += wood - mid
    
    if diff >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)