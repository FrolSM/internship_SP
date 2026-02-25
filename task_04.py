def  sort_list(lst):
    if not lst:
        return lst
    max_index = lst.index(max(lst))
    min_index = lst.index(min(lst))
    lst.append(lst[min_index])
    lst[max_index], lst[min_index] = lst[min_index], lst[max_index]
    return lst
