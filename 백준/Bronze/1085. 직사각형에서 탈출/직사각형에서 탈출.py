x, y, w, h = map(int, input().split())

len = min(abs(x-w), abs(y-h), abs(0-x), abs(0-y))

print(len)