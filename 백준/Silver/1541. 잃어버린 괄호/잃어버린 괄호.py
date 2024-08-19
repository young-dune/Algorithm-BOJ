arr = input().split('-')
#입력받을 때 -를 기준으로 나눈다 -> +와 -가 섞여있는데 최소값을 구하려면 마이너스 뒤에 모든건 더해주고 빼주면 된다!
res = 0

for i in arr[0].split('+'): #우선 +끼리 구분하여 리스트구성
    res += int(i)
for i in arr[1:]: #결과값에 리스트 처음 요소를 넣고 두번째 요소부터 체크
    for j in i.split('+'): #그 다음값부터는 -해준다.
        res -= int(j)
print(res)