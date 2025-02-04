inputStr = input()
arr = [0 for i in range(26)]

for i in inputStr:
    arr[ord(i.lower()) - ord('a')] += 1

sortedArr = sorted(arr, reverse=True)
answer = '?' if sortedArr[0] == sortedArr[1] else chr(arr.index(max(arr)) + ord('a')).upper()

print(answer)