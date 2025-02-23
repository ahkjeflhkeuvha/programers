import sys

diff, N = map(int, sys.stdin.readline().strip().split())
price_per = float('inf')
price_das = float('inf')


prices = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

for price in prices:
	price_das = min(price[0], price_das)
	price_per = min(price[1], price_per)
	
das_case = (((diff + 11) // 12) * price_das)
per_case = diff * price_per

print(per_case if per_case <= das_case else das_case)