from collections import deque

def get_feedback(correct_answer, guess):
    feedback = []
    for i in range(len(correct_answer)):
        if correct_answer[i] == guess[i]:
            feedback.append("S")
        elif guess[i] in correct_answer:
            feedback.append("B")
        else:
            feedback.append("F")
    return feedback

correct_answer = input()
inputed_answer = input()

answer = deque(list(inputed_answer))
res = get_feedback(correct_answer, inputed_answer)

cnt = 1
while res.count("S") < 4:
    s = [] # 스트라이크인 것 (인덱스, 값)
    cnt += 1
    for i in range(len(answer)):
        if res[i] == "S":
            s.append((i, answer[i]))
            continue
        elif res[i] == "F":
            answer[i] = str((int(answer[i]) + 1) % 10)
            
            while answer.count(answer[i]) > 1:
                answer[i] = str((int(answer[i]) + 1) % 10)

    if "B" in res:
        for idx, val in s:
            answer.remove(val)
        answer.rotate(1)
        for idx, val in s:
            answer.insert(idx, val)    
    res = get_feedback(correct_answer, answer)

print(cnt)