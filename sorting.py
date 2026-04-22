import random

def selection_sort(values):
    copy = values[:]
    n = len(copy)
    iterace = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            iterace += 1
            if copy[j] < copy[min_idx]:
                min_idx = j
        copy[i], copy[min_idx] = copy[min_idx], copy[i]
    return copy, iterace

def bubble_sort(values):
    iterace = 0
    copy = values[:]
    i = 0
    while i < len(copy):
        a = 0
        flag = False
        while a < (len(copy) - 1 - i):
            iterace += 1
            if copy[a] > copy[a+1]:
                copy[a], copy[a+1] = copy[a+1], copy[a]
                flag = True
            a += 1
        i += 1
        if flag == False: return copy, iterace
    return copy, iterace

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def main():
    values = random_numbers(10)
    print(values)
    print(selection_sort(values))
    print(bubble_sort(values))
    return None

if __name__ == "__main__":
    main()


