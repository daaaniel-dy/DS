"""
Compute Postfix
"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0

def cal(a, b, op):
    n1 = float(a)
    n2 = float(b)
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    elif op == '^':
        return int(n1) ^ int(n2)


def compute_postfix(postfix):
    opstack = Stack()
    token_list = postfix.split(' ')

    op = ['+', '-', '/', '*', '^']

    for token in token_list:
        if token in op:
            b = opstack.pop()
            a = opstack.pop()
            tmp = cal(a, b, token)
            opstack.push(tmp)
            if opstack.__len__() == 1 and len(token_list) == 0:
                break
        else:  # operand일 때
            opstack.push(token)

    return opstack.top()

postfix = input()
result = compute_postfix(postfix)
print(format(result, ".4f"))