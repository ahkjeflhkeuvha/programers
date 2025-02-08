n, v = map(int, input().split())
measure = set()

for i in range(1, n//2+1):
    if n%i == 0:
        measure.add(i)
        measure.add(n)

if len(measure) < v:
    print('0')
else:
    print(sorted(measure)[v-1])