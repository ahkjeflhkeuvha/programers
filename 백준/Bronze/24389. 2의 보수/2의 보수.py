N = int(input())
binN = bin(N)[2:]
invN = bin(int(''.join('1' if bit == '0' else '0' for bit in binN), 2) + 1)[2:]
comN = ''.join(['0' for _ in range(len(binN) - len(invN))]) + invN

cnt = 0
for i in range(len(binN)):
    if binN[i] == comN[i]:
        cnt += 1

print(32 - cnt)