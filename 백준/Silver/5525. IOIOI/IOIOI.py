import sys

Pn = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())
S = sys.stdin.readline().strip()

pattern_length = 2 * Pn + 1
count = 0
i = 0
pattern_count = 0 

while i < N - 1:
    if S[i:i+3] == "IOI":
        pattern_count += 1 
        if pattern_count >= Pn:
            count += 1  
        i += 2  
    else:
        pattern_count = 0 
        i += 1

print(count)