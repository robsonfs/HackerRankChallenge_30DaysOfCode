def main():
    n = int(input().strip())
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

    reversed_array = [str(arr[i]) for i in range(len(arr)-1, -1, -1)]

    print(" ".join(reversed_array))
