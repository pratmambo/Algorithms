num_list = list(map(int, input().split()))

index = 0
for i in range(len(num_list)):
    for j in range(i,1,-1):
        if num_list[j] < num_list[j-1]:
            index = j-1
    num_list[j], num_list[index]