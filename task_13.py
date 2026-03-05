import time
from functools import wraps

def cached(max_size=None, seconds=None):
    if not isinstance(max_size, int):
        max_size = None
    if not isinstance(seconds, int):
        seconds = None

    def decorator(func):
        cache = {}
        order = []  # порядок добавления ключей

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal cache, order

            key = (args, tuple(sorted(kwargs.items())))
            current_time = time.time()

            # удаление устаревшие записи
            if seconds is not None:
                keys_to_delete = []
                for k, (value, timestamp) in cache.items():
                    if current_time - timestamp > seconds:
                        keys_to_delete.append(k)

                for k in keys_to_delete:
                    cache.pop(k, None)
                    if k in order:
                        order.remove(k)

            if key in cache:
                value, timestamp = cache[key]
                return value

            # результат
            result = func(*args, **kwargs)

            # добавление в кэш
            cache[key] = (result, current_time)
            order.append(key)

            # проверка переполнения cache
            if max_size is not None:
                while len(order) > max_size:
                    oldest = order.pop(0)
                    cache.pop(oldest, None)

            return result

        return wrapper

    return decorator
