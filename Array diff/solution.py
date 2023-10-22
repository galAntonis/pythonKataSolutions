def array_diff(a, b):
	ret_list = []
	for i in a:
		if i not in b:
			ret_list.append(i)
	print(ret_list)

array_diff([1,2,2,2,3],[2])
