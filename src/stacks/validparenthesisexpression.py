def valid_parenthesis_expression(s: str) -> bool:
    stack = []
    for e in s:
        if e in ('(', '[', '{'):
            stack.append(e)
        else:
            if not stack:
                return False
            last = stack.pop()
            if e == ')':
                if last != '(':
                    return False
            elif e == ']':
                if last != '[':
                    return False
            else:
                if last != '{':
                    return False
    return True if not stack else False
