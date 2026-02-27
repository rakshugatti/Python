""" Compare performance of Python List vs NumPy Array
    for summing 1 million elements.
"""

import time
import numpy as np


def main():

    n = 1_000_000  # 1 million elements

    # ----------------------------------
    # Python List Performance
    # ----------------------------------
    python_list = list(range(n))

    start_time = time.time()
    total_list = sum(python_list)
    end_time = time.time()

    list_time = end_time - start_time

    print("Python List Sum:", total_list)
    print("Time taken by Python List:", list_time, "seconds")

    print("\n" + "-" * 50)

    # ----------------------------------
    # NumPy Array Performance
    # ----------------------------------
    numpy_array = np.arange(n)

    start_time = time.time()
    total_numpy = np.sum(numpy_array)
    end_time = time.time()

    numpy_time = end_time - start_time

    print("NumPy Array Sum:", total_numpy)
    print("Time taken by NumPy Array:", numpy_time, "seconds")

    print("\n" + "-" * 50)

    # ----------------------------------
    # Performance Comparison
    # ----------------------------------
    if numpy_time < list_time:
        print("NumPy is faster by", list_time - numpy_time, "seconds")
    else:
        print("Python List is faster by", numpy_time - list_time, "seconds")


if __name__ == "__main__":
    main()