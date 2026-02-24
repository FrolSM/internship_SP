def max_odd(array):
    max_value = None

    for x in array:
        if isinstance(x, (int, float)):
            if x == int(x):
                if int(x) % 2 != 0:
                    if max_value is None or int(x) > max_value:
                        max_value = int(x)

    return max_value
