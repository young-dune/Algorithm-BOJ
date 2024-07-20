n = int(input())
arr = []

for _ in range(n):
    age,name = input().split()
    arr.append([int(age),name])

arr.sort(key= lambda x:x[0])
#lambda함수 = lambda 인자 : 표현식 / map함수와 함께 리스트의 모든 요소에 함수를 적용한 결과값을 반환하는 역할로 사용 가능. 이는 첫 번째 요소에 대해서만 정렬하는 용도로 사용됨.

for age,name in arr:
    print(age,name)