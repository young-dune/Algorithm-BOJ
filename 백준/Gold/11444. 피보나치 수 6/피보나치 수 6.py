import sys
input = sys.stdin.readline

MOD = 1000000007

n = int(input())
matrix = [[1, 1], [1, 0]]

def matmul(mat1, mat2):
    result = [[0] * 2 for _ in range(2)]  # 2차원 배열 생성
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += mat1[i][k] * mat2[k][j]
                result[i][j] %= MOD  # 모듈러 연산 수행
    return result

def dq(a, b):
    if b == 1:
        return a
    powNum = dq(a, b // 2)
    powNum = matmul(powNum, powNum)
    if b % 2 != 0:  # b가 홀수
        powNum = matmul(powNum, a)
    return powNum

if n == 0:
    print(0)
else:
    resultAll = dq(matrix, n)
    print(resultAll[0][1])
