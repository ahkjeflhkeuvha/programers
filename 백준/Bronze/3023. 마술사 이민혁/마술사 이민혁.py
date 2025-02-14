r, c = map(int, input().split())


sample = []

for i in range(r):
    temp = input()
    sample.append(temp + temp[::-1])

a, b = map(int, input().split())

sample.extend(list(reversed(sample)))
sample = [list(row) for row in sample]
sample[a-1][b-1] = '#' if sample[a-1][b-1] == '.' else '.'
sample = [''.join(row) for row in sample]
sample = '\n'.join(sample)
print(sample)