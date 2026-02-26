def sort_list(lst):
    if not lst:
        return lst
    max_value = max(lst)
    min_value = min(lst)

    new_lst = [max_value if el == min_value else min_value if el == max_value else el for el in lst]
    new_lst.append(min_value)
    return new_lst
