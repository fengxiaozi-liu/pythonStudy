def count_num_times(a_list):
    num_count_dict = {}
    max_num_list = []
    for each in a_list:
        if each in num_count_dict.keys():
            num_count_dict[each] += 1
        else:
            num_count_dict[each] = 1
    for key, value in num_count_dict.items():
        if value == max(num_count_dict.values()):
            max_key = key
            max_num_list.append(max_key)
    return max_num_list


if __name__ == '__main__':
    result = count_num_times([1, 6, 7, 3, 2, 5, 8, 1, 3])
    print(result)
