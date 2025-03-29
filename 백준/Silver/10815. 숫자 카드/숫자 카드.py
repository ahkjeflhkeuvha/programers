N = int(input())
cards = {card : 1 for card in list(map(int, input().split()))}
M = int(input())
chk = list(map(int, input().split()))

print(*[1 if card in cards else 0 for card in chk], sep=" ")