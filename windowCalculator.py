from tkinter import Tk, Label, Button, Entry, StringVar
from functools import partial

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

def do_something():
    value = compute_postfix(infix_to_postfix(expr.get()))
    total.set("{0:.4f}".format(value))
    return

root = Tk()
root.title("My Calculator")
expr = StringVar()
title_label = Label(root, text="My Calcualtor").grid(row=0, columnspan=2)
input_exam = Label(root, text="Space between terms: ( 3 + 2 ) * 8").grid(row=1, columnspan=2)
exp_entry = Entry(root, textvariable=expr).grid(row=2, column=0)
total_label = Label(root, text="TOTAL").grid(row=3, column=0)
total = StringVar()
total.set('0')
value_label = Label(root, textvariable=total, width=20).grid(row=3, column=1)
equal_btn = Button(root, text=' = ', width=20, command=do_something).grid(row=2, column=1)
root.mainloop()
root.destroy()