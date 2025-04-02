import re

N = int(input())

for _ in range(N):
    password = str(input().strip())
    print("yes" if 6 <= len(password) <= 9 and re.search(r"\w{6,9}", password) != None else 'no')
    
