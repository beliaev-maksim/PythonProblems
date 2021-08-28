import random

# generate 2 sequences
list1 = [random.randint(0, 100) for i in range(20)]
list2 = [random.randint(0, 100) for i in range(20)]

combined_list = sorted(list1 + list2)  # make list sorted to have ascending order
print(combined_list)

# generate 2d list for all 10s including 100
list_2d = []
for i in range(11):
    list_2d.append([])

index = 0
for elem in combined_list:
    index = int(elem/10)
    list_2d[index].append(elem)

for elem in list_2d:
    perc_of_total = len(elem)/len(combined_list)*100
    print(perc_of_total)

