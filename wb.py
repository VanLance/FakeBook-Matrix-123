def add_to_list_nums(num_list):
    return [int(n) for n in str(int(''.join(str(num)for num in num_list)) + 1)]

print(add_to_list_nums([4,3,2,1]))