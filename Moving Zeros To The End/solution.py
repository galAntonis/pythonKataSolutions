def move_zeros(lst):
    ret_lst = []
    zeros_count = 0
    for i in lst:
        if i == 0:
            zeros_count += 1
        else:
            ret_lst.append(i)
    for i in range(zeros_count):
        ret_lst.append(0)
    return ret_lst
    

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
