import sys

n = int(sys.stdin.readline().strip())

times = []

for _ in range(n):
    start, end = map(int, sys.stdin.readline().strip().split())
    times.append((start, end))

times = sorted(times, key=lambda x: (x[1], x[0]))

cnt = 1
prev_end = times[0][1]

for time in times[1:]:
    start, end = time

    if prev_end <= start:
        if start == end:
            cnt += 1
            continue
        cnt += 1
        prev_end = end

print(cnt)