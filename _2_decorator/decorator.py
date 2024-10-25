from functools import wraps

from _1_algorithm.lru_cache import LRUCache


def lru_cache(maxsize=128):
    cache = LRUCache(maxsize)

    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            # Преобразуем аргументы в кортеж для использования в качестве ключа

            # Проверяем наличие результата в кэше
            cached_value = cache.get(args)
            if cached_value != -1:
                print('Cache hit')
                return cached_value

            # Если результата нет, вызываем функцию
            result = func(*args)
            cache.put(args, result)
            return result

        return wrapper

    return decorator
