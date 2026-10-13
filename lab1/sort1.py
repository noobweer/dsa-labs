# Пирамидальная ("на месте") (массив)
import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def sift_down(arr, n, i):
    while 2 * i + 1 < n:
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if arr[largest] < arr[left]:
            largest = left

        if right < n and arr[largest] < arr[right]:
            largest = right

        if largest == i:
            break

        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        sift_down(arr, i, 0)

    return arr

def read_data(filename):
    records = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            raw_date, fio, num = parts[0], parts[1], parts[2]

            d_parts = raw_date.split('.')
            date_key = (int(d_parts[2]), int(d_parts[1]), int(d_parts[0]))

            records.append((date_key, fio, int(num), line_num, line))
    return records

def write_data(filename, arr, extraline):
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(f"{line[4]},{line[3]}\n" for line in arr)
        f.write(extraline)

if __name__ == "__main__":
    input_arr = read_data(os.path.join(BASE_DIR, "input.txt"))

    start = time.perf_counter()
    sorted_arr = heap_sort(input_arr)
    end = time.perf_counter()

    write_data(os.path.join(BASE_DIR, "output_sort1.txt"), sorted_arr, f"{end - start:.6f} sec")
