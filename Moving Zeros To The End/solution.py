def move_zeros(lst):
    ret_lst = []
    zeros_count = 0
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(i)
            counter += 1
    return ret_lst
    

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
