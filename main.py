# Find Duplicates


data_list = [1, 2, 3, 4, 2, 5, 6, 6, 7, 2, 1, 4, 9]


def find_duplicates(data):
    len_list = len(data)
    results = []
    for i in range(len_list):
        k = i + 1
        for j in range(k, len_list):
            if (data[i] == data[j]) and (data[i] not in results):
                results.append(data[i])

    return results


print(find_duplicates(data_list))