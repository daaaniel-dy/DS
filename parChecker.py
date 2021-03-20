"""
스택활용예1 : 괄호짝맞추기
입력된 수식의 왼쪽 괄호와 오른쪽 괄호를 확인하고
두 괄호의 짝이 맞다면 True, 아니면 False 출력
"""

class Stack:
    def __init__(self):
        self.items = [] # 데이터 저장을 위한 리스트 준비
    def push(self, val):
        self.items.append(val)
    def pop(self):
        try:    # pop할 아이템이 없으면
            return self.items.pop()
        except IndexError:  # indexError 발생
            print("Stack is empty")
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")
    def __len__(self):  # len()로 호출하면 stack의 item 수 반환
        return len(self.items)
    def isEmpty(self):
        return self.__len__() == 0

# 괄호짝을 확인하는 함수 parChecker
def parChecker(parSeq):
    S = Stack()
    for i in parSeq:
        if(i == "("):   # 왼쪽 괄호가 입력된 경우
            S.push(i)
        else:   # 오른쪽 괄호가 입력된 경우
            if(S.isEmpty()):    # 앞서 입력된 왼쪽 괄호가 없다면
                return False
            else:   # 앞서 입력된 왼쪽 괄호가 있다면
                S.pop()
    if (S.isEmpty()):   # Stack이 빈 경우

        return True
    else:
        return False

infixList = list(input())
parSeq = [] # 괄호들을 저장할 리스트

# 수식의 연산자들 중 괄호만 따로 저장
for i in infixList:
    if(i == "(" or i == ")"):
        parSeq.append(i)

print(parChecker(parSeq))