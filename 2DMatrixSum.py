"""
[수행시간 체험 2]
2차원 합 계산

1이상 5000이하의 값 n을 입력받아
리스트 A에 n개의 0부터 100사이의 임의의 랜덤 수를 저장

nXn의 이차원 리스트 B생성
모든 i<=j에 대해, B[i][j] = A[i] + ... + A[j]를 수행하는 함수 sum 생성

sum함수의 수행시간 측정
"""

import time         # 시간 측정을 위한 time module
import random       # 난수 생성을 위한 random module
import numpy as np  # 이차원 배열 생성을 위한 numpy module

# 2차원 리스트 B에 A의 합을 저장하는 sum 함수
def sum(A, B, n):
    tmp = A.copy()
    for i in range(n):
        for j in range(i, n):
            if (i == 0 and j == 0): # B[0][0]의 경우 예외처리
                B[i][j] = tmp[0]
            else:
                tmp[j] = tmp[j] + tmp[j - 1]
                B[i][j] = tmp[j]
        tmp = A.copy()
    print(B)

n = int(input("input n(1<=n<=5000) : "))    # n값 입력

A = list()

random.seed(0)  # 난수 제어를 위한 난수시드

# 리스트 A에 난수 저장
for i in range(n):
    A.append(random.randint(0, 100))
print(A)

B = np.zeros((n, n), dtype=int) # 2차원 배열 B

# sum 수행시간 측정
before = time.process_time()
sum(A, B, n)
after = time.process_time()
print(after - before)