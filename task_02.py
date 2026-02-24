def coincidence(list=None, range=None):
    if list is None or range is None:
        return []
    max_num = max(range)
    min_num = min(range)
    result = [el for el in list if isinstance(el, (int, float)) and min_num <= el <= max_num]
    return result
