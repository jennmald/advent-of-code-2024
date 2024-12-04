import numpy as np

data = np.genfromtxt("day1_data.txt", delimiter="   ")
list1, list2 = zip(*data)

list1 = list(list1)
list2 = list(list2)

distances = [x * (list2.count(x)) for x in list1]

total_sum = sum(distances)

print(total_sum)

