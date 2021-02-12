import random
from matplotlib import pyplot as plt
import matplotlib.colors as mcolors
import time
import numpy as np
global times
times = True
global n
global bms_o_n
global bin_o_n
global start
n = []
bms_o_n = []
bin_o_n = []


def binary_monkey_search(arr, bot, top, x):
    ops = 0
    while bot <= top:
        ops += 1
        monkey = random.randint(bot, top)
        if arr[monkey] == x:
            return [monkey, ops]
        elif arr[monkey] < x:
            bot = monkey + 1
        else:
            top = monkey - 1
    return -1 # not in array


def binarySearch(arr, l, r, x):
    ops = 0
    while l <= r:
        ops += 1
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return [mid, ops]
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def make_random_array(length):
    rand_top = length * 10
    ret = [0 for _ in range(length)]
    for i in range(length):
        if times and i % (length/10) == 0:
            print(f"generation {i} at time {time.time() - start}")
        ret[i] = random.randint(0, rand_top)
    ret = list(set(ret))
    ret.sort()
    return ret


def get_random_array(arr):
    length = len(arr) - 1
    mid = int(len(arr)/2)
    bot = random.randint(0, mid)
    top = random.randint(mid + 1, length)
    return arr[bot:top]


def test_random():
    global n
    global bms_o_n
    global bin_o_n
    global start
    start = time.time()
    main_arr = make_random_array(10000000)
    if times:
        print(f"main arr generated at time {time.time() - start} with size {len(main_arr)}")
    for i in range(10000):
        if times:
            print(f"try {i} at time {time.time() - start}")
            # arr_start = time.time()
        arr = get_random_array(main_arr)
        search = random.randint(0, len(arr) - 1)
        # if times:
        #     print(f"try {i} made array of size {len(arr)} in {time.time() - arr_start} seconds")
        #     bms_start = time.time()
        out = binary_monkey_search(arr, 0, len(arr)-1, arr[search])
        # if times:
        #     print(f"try {i} bms finished in {time.time() - bms_start}")
        out2 = binarySearch(arr, 0, len(arr) - 1, arr[search])
        # print(search)
        # print(out)
        n.append(len(arr))
        bms_o_n.append(out[1])
        bin_o_n.append(out2[1])
    print(f"finished everything at {time.time() - start}")

    fout = open("bms_out.txt", "w")
    fout.write(str(len(n)) + "\n")
    fout.write(" ".join(map(str, n)) + "\n")
    fout.write(" ".join(map(str, bms_o_n)) + "\n")
    fout.write(" ".join(map(str, bin_o_n)))


def read_random():
    global n
    global bms_o_n
    global bin_o_n
    fin = open("bms_out.txt", "r")
    length = int(fin.readline())
    n = list(map(int, fin.readline().split()))
    bms_o_n = list(map(int, fin.readline().split()))
    bin_o_n = list(map(int, fin.readline().split()))


def graph_random():
    global n
    global bms_o_n
    global bin_o_n
    plt.scatter(n, bms_o_n, color="red", s=4)
    plt.scatter(n, bin_o_n, color="blue", s=4)
    # m, b = np.polyfit(n, bms_o_n, 1)
    # n = np.array(n)
    # plt.plot(n, m*n + b, color="red")
    # m, b = np.polyfit(n, bin_o_n, 1)
    # plt.plot(n, m*n + b, color="blue")
    plt.xlabel("n, or length of list")
    plt.ylabel("operations")
    plt.show()


def test_all():
    global n
    global bms_o_n
    global bin_o_n
    global start
    start = time.time()
    main_arr = make_random_array(10000)
    for i in range(len(main_arr)):
        if times:
            print(f"try {i} at time {time.time() - start}")
        for _ in range(100):
            out = binary_monkey_search(main_arr, 0, len(main_arr)-1, main_arr[i])
            out2 = binarySearch(main_arr, 0, len(main_arr) - 1, main_arr[i])
            n.append(i)
            bms_o_n.append(out[1])
            bin_o_n.append(out2[1])
    fout = open("test_all_out.txt", "w")
    fout.write(str(len(n)) + "\n")
    fout.write(" ".join(map(str, n)) + "\n")
    fout.write(" ".join(map(str, bms_o_n)) + "\n")
    fout.write(" ".join(map(str, bin_o_n)))


def read_all():
    global n
    global bms_o_n
    global bin_o_n
    fin = open("test_all_out.txt", "r")
    length = int(fin.readline())
    n = list(map(int, fin.readline().split()))
    bms_o_n = list(map(int, fin.readline().split()))
    bin_o_n = list(map(int, fin.readline().split()))


def test_all_avg():
    global n
    global bms_o_n
    global bin_o_n
    global start
    start = time.time()
    main_arr = make_random_array(10000)
    for i in range(len(main_arr)):
        if times:
            print(f"try {i} at time {time.time() - start}")
        avg = 0
        for _ in range(10):
            out = binary_monkey_search(main_arr, 0, len(main_arr)-1, main_arr[i])
            avg += out[1]
        n.append(i)
        out2 = binarySearch(main_arr, 0, len(main_arr) - 1, main_arr[i])
        bms_o_n.append(float(avg/10))
        bin_o_n.append(out2[1])
    fout = open("test_all_out_avg.txt", "w")
    fout.write(str(len(n)) + "\n")
    fout.write(" ".join(map(str, n)) + "\n")
    fout.write(" ".join(map(str, bms_o_n)) + "\n")
    fout.write(" ".join(map(str, bin_o_n)))


def get_all_avg():
    global n
    global bms_o_n
    global bin_o_n
    num_better = 0
    times_better = 0
    for i in range(len(n)):
        if bms_o_n[i] < bin_o_n[i]:
            num_better += 1
        times_better += bms_o_n[i]/bin_o_n[i]
    percent = float(num_better/len(n) * 100)
    avg_better = times_better/len(n)
    print(f"{percent}% of bms tests were better than binary search")
    print(f"on average, bms took {avg_better} times longer than binary search")


def read_all_avg():
    global n
    global bms_o_n
    global bin_o_n
    fin = open("test_all_out_avg.txt", "r")
    length = int(fin.readline())
    n = list(map(int, fin.readline().split()))
    bms_o_n = list(map(float, fin.readline().split()))
    bin_o_n = list(map(int, fin.readline().split()))


def graph(x_ax, y_ax):
    global n
    global bms_o_n
    global bin_o_n
    plt.scatter(n, bms_o_n, color="red", s=4)
    plt.scatter(n, bin_o_n, color="blue", s=4)
    # m, b = np.polyfit(n, bms_o_n, 1)
    # n = np.array(n)
    # plt.plot(n, m*n + b, color="red")
    # print(f"binary monkey search: y = {m}x + {b}")
    # m, b = np.polyfit(n, bin_o_n, 1)
    # plt.plot(n, m*n + b, color="blue")
    # print(f"binary search: y = {m}x + {b}")
    plt.xlabel(x_ax)
    plt.ylabel(y_ax)
    plt.show()


read_random()
#get_all_avg()
graph("index in list", "operations")
