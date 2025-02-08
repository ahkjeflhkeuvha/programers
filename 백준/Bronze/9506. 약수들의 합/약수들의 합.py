import sys  

def list_measure(n):
    m_set = set()

    for i in range(1, n//2 + 1):
        if n % i == 0:
            m_set.add(i)
    
    return m_set

def res_str(m):
    s = ""
    for i in range(len(m) - 1):
        s += '{} + '.format(m[i])
    s += '{}'.format(m[-1])

    return s

while True:
    sub = int(sys.stdin.readline().strip())
    if sub == -1:
        break
    m_set = list_measure(sub)
    
    if sum(m_set) == sub:
        s = res_str(list(sorted(m_set)))
        print('{} = {}'.format(sub, s))
    else:
        print('{} is NOT perfect.'.format(sub))

