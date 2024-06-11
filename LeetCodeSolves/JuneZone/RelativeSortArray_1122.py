def relativeSortArray(arr1, arr2):
    position_map = {value: index for index, value in enumerate(arr2)}

    sorted_arr1 = sorted(arr1, key=lambda x: position_map.get(x, 1000 + x))
    return sorted_arr1


if __name__ == '__main__':
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    print(relativeSortArray(arr1, arr2))