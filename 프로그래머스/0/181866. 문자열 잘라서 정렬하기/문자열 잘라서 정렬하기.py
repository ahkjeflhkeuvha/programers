import re
def solution(myString):
    return [s for s in sorted(re.split("[x+]", myString)) if s != ""]