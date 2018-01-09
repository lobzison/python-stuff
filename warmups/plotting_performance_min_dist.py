"""
Plots of performance testing
of finding minimum distance algorythms
"""
import time
import random
import shortest_distance as sd
import matplotlib.pyplot as plt


def gen_tuple_list(num):
    """Generates list of random tuples in format
    (x, y) where x and y >-100 and <100"""
    return [(random.randint(-99, 99), random.randint(-99, 99))
            for _ in range(num)]


def time_run_brute(fnk, runs):
    """Times fnk on upa graph"""
    xval = []
    yval = []
    for n in range(10, runs, 10):
        xval.append(n)
        test_list = gen_tuple_list(n)
        c_time = time.time()
        fnk(test_list)
        time_passed = time.time() - c_time
        yval.append(time_passed)
    return [xval, yval]


def time_run_divide(fnk, runs):
    """Times fnk on upa graph"""
    xval = []
    yval = []
    for n in range(10, runs, 10):
        xval.append(n)
        test_list = gen_tuple_list(n)
        c_time = time.time()
        test_list.sort(key=lambda x: x[0])
        fnk(test_list)
        time_passed = time.time() - c_time
        yval.append(time_passed)
    return [xval, yval]


def plot():
    runs = 200
    time_brute = time_run_brute(sd.brute_force, runs)
    time_divide = time_run_divide(sd.divide_and_conquer, runs)
    plt.plot(time_brute[0], time_brute[1], '-r', label="Brute force time")
    plt.plot(time_divide[0], time_divide[1], '-g', label="Divide time")
    plt.xlabel("Number of points in set")
    plt.ylabel("Runtime")
    plt.show()



if __name__ == "__main__":
 	plot()
