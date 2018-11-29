num_list = list(map(int, input().split()))

index = 0
for i in range(len(num_list)):
    min = num_list[i]
    for j in range(i, len(num_list)):
        if num_list[j] < min:
            min = num_list[j]
            index = j
    num_list[i], num_list[index] = num_list[index], num_list[i]
print(num_list)