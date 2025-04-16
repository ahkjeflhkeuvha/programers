N = int(input())

if -pow(2, 15) <= N <= pow(2, 15) - 1:
    print("short")
elif -pow(2, 31) <= N <= pow(2, 31) - 1:
    print("int")
else:
    print("long long")