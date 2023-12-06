import time
import sys
import copy

#use csv and dump into excel

def read_file(file_name):
    f = open(file_name, 'r')
    line = f.readline()
    #need to make the strings ints
    mapped = map(int, line.split(", "))
    a_list = list(mapped)
    return a_list

    #want this to return a list that we can use for sorts

def print_list(list):
    for i in range(len(list)):
        if i+1 == len(list):
            print(str(list[i]), end='')
            return
        else:
            print(str(list[i]) + ", ", end='')

def selection_sort(list):
    start = time.time()
    for i in range(len(list)):
        #index of minimum number for iteration
        min_index = i
        for j in range(i+1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    end = time.time()
    rounded = round((end-start), 2)
    print("Selection Sort (" + str(rounded) + " ms): ", end='')
    print_list(list)
    #added for anaylsis below
    return rounded

def insertion_sort(list):
    start = time.time()
    for i in range(1, len(list)):
        key = list[i]

        j = i-1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j+1] = key
    end = time.time()
    rounded = round((end - start), 2)
    print("Insertion Sort (" + str(rounded) + " ms): ", end='')
    print_list(list)
    # added for anaylsis below
    return rounded

def merge_sort(list):
    length = len(list)
    if length == 1:
        return list

    mid = length // 2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])

    return merge(left, right)

def merge(left, right):
    output = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i+=1
        else:
            output.append(right[j])
            j+=1

    output.extend(left[i:])
    output.extend(right[j:])
    return output



def main():
    init_list = read_file(sys.argv[1])
    # pass the list we get from read file to the sorts (make sure you don't pass the sorted list to the next sort)
    # instead create deep copies of the list
    ss_list = copy.deepcopy(init_list)
    insertion_list = copy.deepcopy(init_list)
    merge_list = copy.deepcopy(init_list)
    selection_sort(ss_list)
    print('')
    insertion_sort(insertion_list)
    print('')
    start = time.time()
    sorted = merge_sort(merge_list)
    end = time.time()
    rounded = round((end - start), 2)
    print("Merge Sort     (" + str(rounded) + " ms): ", end='')
    print_list(sorted)

main()


