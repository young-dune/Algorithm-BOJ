arr = input().split('-')
res = 0

for i in arr[0].split('+'): 
    res += int(i)
for i in range(1,len(arr)):
    for j in arr[i].split('+'): 
        res -= int(j)
        
print(res)