N = int(input())
cards = {}
for key in input().split():
    cards[int(key)] = cards.get(int(key), 0) + 1

S = int(input())
S_cards = list(map(int, input().split()))

cnt_cards = [cards.get(s, 0) for s in S_cards]
print(*cnt_cards, sep=" ")