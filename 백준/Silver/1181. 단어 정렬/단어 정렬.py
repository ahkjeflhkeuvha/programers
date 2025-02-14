n = int(input())
dic = []

for _ in range(n):
    word = input()

    if word not in dic:
        dic.append(word)
    
dic = sorted(dic, key = lambda x : (len(x), x))

for word in dic:
    print(word)