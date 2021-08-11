# 10818 최소, 최대
def bubbleSort(x):
    for i in range(len(x)-1, 0, -1):
        for j in range(i):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x

def selectionSort(x):
    for i in range(0, len(x)-1):
        min_idx = i
        for j in range(i+1, len(x)):
            if x[min_idx] > x[j]:
                min_idx = j
        x[i], x[min_idx] = x[min_idx], x[i]
    return x  

def quickSort(x):
    if len(x) <= 1:
        return x
    
    base = x[len(x)//2]
    small, equal, big = [], [], []

    for i in x:
        if i < base:
            small.append(i)
        elif i > base:
            big.append(i)
        else:
            equal.append(i)
    
    return quickSort(small) + equal + quickSort(big)


N = int(input())
numbers = list(map(int, input().split()))

sorted = quickSort(numbers)

print(sorted[0], sorted[-1])