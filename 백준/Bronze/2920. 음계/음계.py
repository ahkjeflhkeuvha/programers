scale = list(map(int, input().split()))

if all(scale[i] + 1 == scale[i+1] for i in range(len(scale) - 1)):
    print("ascending")
elif all(scale[i] - 1 == scale[i+1] for i in range(len(scale) - 1)):
    print("descending")
else:
    print("mixed")