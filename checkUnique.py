"""
[시간 복잡도 체험]
유일성 검사 문제

-n부터 n사이의 정수 n개가 임의로 저장된 리스트 A에서
모든 값들이 서로 다르면 YES, 같은 값이 한 쌍 이상 존재하면 No 출력

def unique_n2 : 이중 반복문을 사용해 O(n^2)동안 동작
def unique_nlogn : .sort()로 정렬한 후 단일 반복문을 사용해 O(nlogn)동안 동작
def unique_n : 새로운 리스트 B를 정의해 O(n)동안 동작
"""

import random   # 난수 생성을 위한 random module
import time     # 시간 측정을 위한 time module

# 이중 반복문을 사용한 함수
def unique_n2(A, n):
    flag = 0
    for i in range(n - 1):
        for j in range(i, n - 1):
            if (A[i] == A[j + 1]):
                print("No")
                flag = 1
                break
            else:
                pass
        if(flag == 1):
            break
    if(flag == 0):
        print("Yes")

# .sort()를 사용한 함수
def unique_nlogn(A, n):
    A.sort()
    pivot = 0
    for i in range(1, n):
        if(A[pivot] == A[i]):
            print("No")
            break
        else:
            pivot += 1
    if(pivot == n-1):
        print("Yes")

# 새로운 리스트(자료형)를 사용한 함수
def unique_n(A):
    B = set(A)
    if(len(A) == len(B)):
        print("Yes")
    else:
        print("No")

random.seed(0)  # 난수 제어를 위한 난수 시드

n = int(input("input n(2<=n<=100000) : "))

A = random.sample(range(-n, n + 1), n)  # 리스트에 난수 저장
print(A)

# unique_n2 수행시간 측정
start = time.process_time()
unique_n2(A, n)
end = time.process_time()
print("process time : ", end - start)

# unique_nlogn 수행시간 측정
start = time.process_time(
)
unique_nlogn(A, n)
end = time.process_time()
print("process time : ", end - start)

# unique_n 수행시간 측정
start = time.process_time()
unique_n(A)
end = time.process_time()
print("process time : ", end - start)
