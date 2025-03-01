N = input()
cars = list(input().split())
cnt = 0

for car in cars:
    if car.endswith(N):
        cnt += 1

print(cnt)