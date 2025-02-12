from collections import deque

def chk_bracket(bracket):
    queue = []
    for s in bracket:
        if s == "(" or s == "{" or s == '[':
            queue.append(s)
        elif s == ")":
            if len(queue) != 0 and queue[-1] == "(":
                queue.pop()
            else:
                return False
        elif s == "}":
            if len(queue) != 0 and queue[-1] == "{":
                queue.pop()
            else:
                return False
        elif s == "]":
            if len(queue) != 0 and queue[-1] == "[":
                queue.pop()
            else:
                return False
            
    return True if len(queue) == 0 else False

def solution(s):
    answer = 0
    
    bracket = deque(list(s))
    
    for i in range(len(s)):
        res = chk_bracket(list(bracket))
        if res:
            answer += 1
        bracket.rotate(1)
        
    return answer