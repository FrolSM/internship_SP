def connect_dicts(dict1, dict2):
    sum1 = sum(dict1.values())
    sum2 = sum(dict2.values())

    if sum1 > sum2:
        result = dict2.copy()
        for k, v in dict1.items():
            result[k] = v
    else:
        result = dict1.copy()
        for k, v in dict2.items():
            result[k] = v

    filter_items = {k: v for k, v in result.items() if v >= 10}
    sorted_items = sorted(filter_items.items(), key=lambda x: x[1])
    result_dict = dict(sorted_items)

    return result_dict
