import math
w, h = map(int, input().split())

circul = 2*w + h*math.pi

print(math.floor(circul))