import numpy as np

original = [1,3,2,4,6,9,7,8,5]

sort = original.copy()

def getMin(list):
    min = 10
    for i, x in enumerate(list):
        if x < min:
            min = x
            idx = i
    print(min)
    list.remove(min)
    return min
res = []
for i in range(len(original)):
    res.append(getMin(sort))
print(res)