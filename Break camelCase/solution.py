def solution(s):
    string_lst = []
    for i in s:
        if i.isupper():
            string_lst.append(" ")
        string_lst.append(i)
    str_ret = "".join(string_lst)
    return str_ret

solution("camelCasing")
