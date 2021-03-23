class deque:
    def __init__(self, s):
        self.items = s
        self.front_index = 0

    def append(self, c):
        self.items.append(c)

    def appendleft(self, c):
        self.items.insert(self.front_index, c)

    def pop(self):
        if len(self.items) == 0 or self.front_index == len(self.items):
            print("Queue is empty")
        else:
            return self.items.pop()

    def popleft(self):
        if len(self.items) == 0 or self.front_index == len(self.items):
            print("Queue is empty")
        else:
            x = self.items[self.front_index]
            self.front_index += 1
            return x

    def left(self):
        if len(self.items) == 0 or self.front_index == len(self.items):
            print("Queue is empty")
        else:
            return self.items[self.front_index]

    def right(self):
        if len(self.items) == 0 or self.front_index == len(self.items):
            print("Queue is empty")
        else:
            return self.items[-1]

    def __len__(self):
        return len(self.items) - self.front_index

def check_palindrome(s):
    dq = deque(s)
    palindrome = True
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            palindrome = False
    return palindrome

s = list(input())
print(check_palindrome(s))