def getSecond(list):
    max = list[0] >= list[1] and list[0] or list[1]
    second = list[0] < list[1] and list[0] or list[1]
    index = 2;
    while index<len(list):
        if list[index] >= max:
            second = max
            max = list[index]     
        elif list[index] < max and list[index] >= second:
            second = list[index]
        index = index + 1
    return second

print(getSecond([1,2,3]))
print(getSecond([2,1,3]))
print(getSecond([3,2,3]))

print(getSecond([1,200,3]))

print(getSecond([3,3,3]))
