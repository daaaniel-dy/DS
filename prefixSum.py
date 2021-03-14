"""
[수행시간 체험 1]
두 버전의 prefix sum 수행시간 비교

prefix sum S[i]는
S[i] = X[0] + X[1] + ... + X[i]

prefixSum1(X, n)의 알고리즘은 이중반복문을 사용
for i = 0 to n-1 do
    S[i] = 0
    for j = 0 to i do
        S[i] += A[j]

prefixSum2(X, n)의 알고리즘은 하나의 반복문 사용
for i = 1 to n-1 do
    S[i] = S[i-1] + A[j]
"""

import time   # 시간 측정을 위한 time module
import random # 난수 생성을 위한 random module

# 이중반복문을 사용한 함수
def prefixSum1(X, n):
  for i in range(n):
    S.append(0)
    for j in range(i+1):
      S[i] += X[j]

# 하나의 반복문을 사용한 함수
def prefixSum2(X, n):
  S.append(X[0])
  for i in range(1, n):
    S.append(0)
    S[i] = S[i-1] + X[i]

random.seed(0)  # 난수 제어를 위한 난수 시드

n = int(input("input Number of int : "))
X = list()

# 리스트 X에 난수 저장
for i in range(n):
  randN = random.randint(-999, 999)
  X.append(randN)

S = list()  # 빈 리스트 S 생성

# prefixSum1 수행시간 측정
before = time.process_time()
prefixSum1(X, n)
after = time.process_time()
print(after - before)
S.clear()

# prefixSum2 수행시간 측정
before = time.process_time()
prefixSum2(X, n)
after = time.process_time()
print(after - before)
S.clear()
