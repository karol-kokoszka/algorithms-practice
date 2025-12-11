from typing import List

def evaluate_expression(s: str) -> int:
    stack = []
    rpn_expression = transform_to_rpn(s)
    for elem in rpn_expression:
        if is_operand(elem):
            a = stack.pop()
            b = stack.pop()
            stack.append(compute(b, elem, a))
        else:
            stack.append(elem)
    return stack.pop() if stack else 0

def transform_to_rpn(s: str) -> List[any]:
    op_prio = {'-': 1, '(': 0, '+': 1, '/': 2, '*': 2, '%': 2, '^': 3}
    rpn = []
    stack = []
    i = 0
    positive, openedParenthesis = True, False
    while i < len(s):
        if s[i].isdigit():
            j = 0
            while i+j < len(s) and s[i+j].isdigit():
                j += 1
            rpn.append(s[i:i+j] if positive else '-' + s[i:i+j])
            openedParenthesis = False
            positive = True
            i += j
        elif is_operand(s[i]):
            if s[i] == '-':
                # beginning of the expression -> nothing on output yet 
                # OR first operand after ( 
                if not rpn or openedParenthesis:
                    positive = False
                    i += 1
                    continue
            while stack and op_prio[stack[-1]] >= op_prio[s[i]]:
                rpn.append(stack.pop())
            stack.append(s[i])
            i += 1
        elif s[i] == '(':
            openedParenthesis = True
            stack.append(s[i])
            i += 1
        elif s[i] == ')':
            while stack and stack[-1] != '(':
                rpn.append(stack.pop())
            stack.pop()
            i += 1
    while stack:
        rpn.append(stack.pop())
    return rpn

def is_operand(c: str) -> bool:
    return c in ['-', '+', '/', '*', '^', '%']

def compute(left: str, op: str, right: str) -> int:
    if op == '-':
        return int(left) - int(right)
    elif op == '+':
        return int(left) + int(right)
    elif op == '*':
        return int(left) * int(right)   
    elif op == '/':
        return int(left) / int(right)   
    elif op == '%':
        return int(left) % int(right)   
    elif op == '^':
        return int(left) ** int(right)   
     