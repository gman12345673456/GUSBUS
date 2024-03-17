# standard algorythmys
# accepted ways of solving particular problems

# linear search *
# binary search *
# Permutation *
# Merge sort *
# find min/max *
# selection *

def linearsearch(arr):
    found = False
    i = 0
    search_term = int(input())
    while found == False and i < len(arr):
        if arr[i] == search_term:
            found = True
            i += 1
        return found




arr = [7, 4, 8, 18, 19, 5, 29, 348, 32, 63]

print(linearsearch(arr))


def shorter_linear(arr):
    found = False
    search_term = int(input())
    for i in arr:
        if i == search_term:
            found = True
            break 
    return found
shorter_linear(arr)