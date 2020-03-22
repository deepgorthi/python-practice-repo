def get_all_substrings(string):
    length = len(string)
    alist = []
    for i in range(length):
        for j in range(i, length):
            alist.append(string[i:j+1])
    return alist

print(get_all_substrings('abcde'))
