def base(n, k):
    realNum = ""
    
    while n:
        remainder = n%k
        realNum = str(remainder) + realNum
        n //= k
    
    return realNum

def prime(l, s):
    answer = 0
    for k in l:
        if len(k) == 0 or int(k) < 2:
            continue
        chk = True
        for i in range(2,int(int(k)**0.5)+1):
            if int(k)%i==0:
                chk=False
                break
        if chk:
            answer+=1
            
    return answer

def solution(n, k):
    base_str = base(n, k)
    answer = prime(base_str.split('0'), base_str)
    return answer