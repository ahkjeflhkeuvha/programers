from collections import deque
n = int(input())

card = deque(list(range(1, n + 1)))

while len(card) != 1:
    card.popleft()
    t = card.popleft()
    card.append(t)

    if len(card) == 1:
        break

print(card[0])