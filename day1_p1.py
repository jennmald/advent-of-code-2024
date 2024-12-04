import numpy as np

data = np.genfromtxt("day1_data.txt", delimiter="   ")
list1, list2 = zip(*data)

list1 = list(list1)
list2 = list(list2)

list1.sort()
list2.sort()

distances = [abs(x - y) for x, y in zip(list1, list2)]

total_sum = sum(distances)

print(total_sum)

