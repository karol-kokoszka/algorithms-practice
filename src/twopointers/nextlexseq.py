from typing import List

def reverse(s: List[str]):              
    for i in range(len(s) // 2):
        s[i], s[-1 - i] = s[-1 - i], s[i]
    
def next_lexicographical_sequence(s: str) -> str:
    s = list(s)
    i = len(s) - 2
    while i >= 0 and s[i] >= s[i+1]:
        i-=1
    if i > -1:
        j = i+1
        while j < len(s) and s[j] > s[i]:
            j+=1
        s[i], s[j-1] = s[j-1], s[i]
    rightPart = s[i+1:]
    reverse(rightPart)
    s[i+1:] = rightPart
    return "".join(s)
