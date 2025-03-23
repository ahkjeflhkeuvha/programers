N = int(input())
people = input()

sec_p = people.count("security")
big_p = people.count("bigdata")

print("security!" if sec_p > big_p else "bigdata?" if big_p > sec_p else "bigdata? security!")