x = int(input())
n = int(input())

tot = x * (n + 1)

for _ in range(n):
    spend = int(input())
    tot -= spend

print(tot)