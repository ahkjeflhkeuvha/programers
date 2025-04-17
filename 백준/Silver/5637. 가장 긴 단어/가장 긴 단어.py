import sys
import re

sentences = []

while True:
    sentence = re.split(r"[^a-zA-Z-]", sys.stdin.readline().strip())
    sentences.extend(sentence)

    if 'E-N-D' in sentences:
        break

print(sorted(sentences, key=lambda x: -len(x))[0].lower())