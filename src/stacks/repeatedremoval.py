from collections import deque

def repeated_removal_of_adjacent_duplicates(s: str) -> str:
    stack = deque()
    for c in s:
        if not stack:
            stack.append(c)
        else:
            if c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
    result = ""
    while stack:
        result += stack.popleft()
    return result
