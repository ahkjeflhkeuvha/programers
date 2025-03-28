N, M = map(int, input().split())
lights = list(map(int, input().split()))

def handle_lights(lights, s, e, c):
    for i in range(s-1, e):
        lights[i] = c
    return lights

def toggle_lights(lights, s, e):
    for i in range(s-1, e):
        lights[i] = abs(lights[i] - 1)
    return lights

for _ in range(M):
    a, i, x = map(int, input().split())

    if a == 1:
        lights[i-1] = x
    elif a == 2:
        lights = toggle_lights(lights, i, x)
    elif a == 3:
        lights = handle_lights(lights, i, x, 0)
    else:
        lights = handle_lights(lights, i, x, 1)


print(*lights, sep=" ")