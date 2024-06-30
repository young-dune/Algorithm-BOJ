student_list = []
result_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
absent_list = []

for _ in range(28):
    n = int(input())
    student_list.append(n)

for i in result_list:
    if i not in student_list:
        absent_list.append(i)

absent_list.sort()

for j in absent_list:
    print(j)