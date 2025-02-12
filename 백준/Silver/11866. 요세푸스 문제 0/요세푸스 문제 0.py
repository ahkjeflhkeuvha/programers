from collections import deque
queue = []

n, k = map(int, input().split())

people = deque(list(range(1, n+1)))

while people:
    people.rotate(-k+1)
    t = people.popleft()
    queue.append(t)


print("<", ', '.join(str(i) for i in queue), ">", sep = '')