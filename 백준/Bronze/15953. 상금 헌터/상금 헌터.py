# 1 -> 3 -> 6 -> 10 -> 15 -> 21
# 500 300  200   50    30    10
n = int(input())

for i in range(n):
    fir, sec = map(int, input().split())
    tot = 0

    if fir == 1:
        tot += 5000000
    elif 2 <= fir <= 3:
        tot += 3000000
    elif 4<= fir <= 6:
        tot += 2000000
    elif 7 <= fir <= 10:
        tot += 500000
    elif 11 <= fir <= 15:
        tot += 300000
    elif 16 <= fir <= 21:
        tot += 100000
    
    if sec == 1:
        tot += 5120000
    elif 2<= sec <= 3:
        tot += 2560000
    elif 4 <= sec <= 7:
        tot += 1280000
    elif 8 <= sec <= 15:
        tot += 640000
    elif 16 <= sec <= 31:
        tot += 320000
    
    print(tot)
    