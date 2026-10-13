import os
import time

from sort1 import BASE_DIR, read_data, write_data


def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        left = 0
        right = i - 1
        val = arr[i]

        while left <= right:
            mid = (left + right) // 2
            if val < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        for j in range(i - 1, left - 1, -1):
            arr[j + 1] = arr[j]
        arr[left] = val

    return arr

if __name__ == "__main__":
    input_arr = read_data(os.path.join(BASE_DIR, "input50.txt"))

    start = time.perf_counter()
    sorted_arr = binary_insertion_sort(input_arr)
    end = time.perf_counter()

    write_data(os.path.join(BASE_DIR, "output_sort2.txt"), sorted_arr, f"{end - start:.6f} sec")
