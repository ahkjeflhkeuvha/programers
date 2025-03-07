N = int(input())
scores = list(map(int, input().split()))

score_dict = {i + 1 : scores[i] for i in range(N)}
score_dict = sorted(score_dict.items(), key=lambda x: -x[1])

print(*[score_dict[i][0] for i in range(3)], sep=" ")