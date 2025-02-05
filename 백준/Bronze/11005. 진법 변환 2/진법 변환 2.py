bNum, base = map(int, input().split())
realNum = ""


while bNum:
    remainder = bNum % base

    if remainder >= 10:
        realNum = chr(remainder + 55) + realNum
    else:
        realNum = str(remainder) + realNum

    bNum //= base


print(realNum)
