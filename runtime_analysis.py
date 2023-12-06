from sort_algs import *
import random
import csv

header = ['increment', 'ss_time', 'is_time', 'ms_time']

def analysis(init_list, num_increment, writer):
    data = []
    ss_list = copy.deepcopy(init_list)
    insertion_list = copy.deepcopy(init_list)
    merge_list = copy.deepcopy(init_list)

    time_ss = selection_sort(ss_list)

    time_is = insertion_sort(insertion_list)

    start = time.time()
    sorted_m = merge_sort(merge_list)
    end = time.time()
    time_ms = round((end - start), 2)

    num_elements = 5000 + num_increment
    data.insert(0, num_elements)
    data.extend((time_ss, time_is, time_ms))
    writer.writerow(data)

def main():
    f = open('sort.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(header)

    # x - axis : length of the sequence
    # y - axis : running time

    increment = 0
    for step in range(0, 500):
        randomlist = []
        for i in range(0, 5000 + increment):
            n = random.randint(-10, 10)
            randomlist.append(n)
        increment += 10
        analysis(randomlist, increment, writer)
    #     randomlist.append(n)
        print(step)
    # print(randomlist)

main()
