n = int(input())
arr = []

for i in range(n):
    s = input()
    arr.append(s)
#set() = 중복을 허락하지 않음 + 순서가 없다.

myList = list(set(arr))
myList.sort()
myList.sort(key = len)

for i in range(len(myList)):
    print(myList[i])