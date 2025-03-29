from collections import deque

N = int(input())
balloons = deque(list(map(int, input().split())))
idx = deque(range(1, N + 1)) # 안에 들어있는 쪽지가 같은 경우
answer = []

while balloons:
    next = balloons.popleft()
    answer.append(idx.popleft())
    if next > 0:
        balloons.rotate(-(next - 1)) # 음수면 -(next - 1)만큼 회전
        idx.rotate(-(next - 1))
    else:
        balloons.rotate(-next)
        idx.rotate(-next)
    
print(*answer, end=" ")