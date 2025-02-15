n, cnt = map(int, input().split())
cables = []

for _ in range(n):
    cables.append(int(input()))

start, end = 1, max(cables)

while start <= end:
    mid = (start + end) // 2
    cable_cnt = 0

    for cable in cables:
        cable_cnt += cable // mid

    if cable_cnt >= cnt:
        start = mid + 1
    else:
        end = mid - 1

print(end)