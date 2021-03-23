'''
Infix to postfix
'''


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


def infix_to_postfix(infix):
    opstack = Stack()
    outstack = []
    token_list = infix.split(' ')
    flag = 0

    # 연산자의 우선순위 설정
    prec = {}
    prec['('] = 0
    prec['+'] = 3
    prec['-'] = 3
    prec['*'] = 2
    prec['/'] = 2
    prec['^'] = 1

    op = ['+', '-', '/', '*', '^']

    for token in token_list:
        if token == '(':
            opstack.push(token)
            flag += 1
        elif token == ')':
            if flag == 0:
                flag -= 1
                break
            while not opstack.isEmpty():
                if opstack.top() == '(':
                    opstack.pop()
                    break
                tmp = opstack.pop()
                outstack.append(tmp)
            flag -= 1
        elif token in op:
            if opstack.isEmpty():
                opstack.push(token)
            else:
                if opstack.top() == '(':
                    opstack.push(token)
                elif prec[opstack.top()] <= prec[token]:
                    while not opstack.isEmpty() and opstack.top() != '(':
                        tmp = opstack.pop()
                        outstack.append(tmp)
                    opstack.push(token)
                else:
                    opstack.push(token)
        elif token == '':
            opstack.pop()
            break
        else:  # operand일 때
            outstack.append(token)

    if flag == 0:
        if opstack.isEmpty():
            return " ".join(outstack)
        else:
            while not opstack.isEmpty():
                tmp = opstack.pop()
                if tmp != '(':
                    outstack.append(tmp)
            return " ".join(outstack)
    else:
        return  " "


infix_expr = input()
postfix_expr = infix_to_postfix(infix_expr)
print(postfix_expr)