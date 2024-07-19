from collections import deque

n = int(input())
trash = [] #버리는 배열
card = [i for i in range(1,n+1)]

while(len(card)!= 1):
    trash.append(card.pop(0)) #먼저 카드 버리기
    card.append(card.pop(0)) #뒤에 카드 빼서 다시 넣기

for i in trash:
    print(i, end=' ')

print(card[0])
