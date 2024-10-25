from functools import wraps


class ListNode:
    def __init__(self, val=0, key=None):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.dummy_head = ListNode(-1, -1)
        self.end = ListNode(-2, -2)
        self.dummy_head.next = self.end
        self.end.prev = self.dummy_head

    def _update_dummy_head(self, val):
        self.dummy_head.next.prev = val
        val.prev = self.dummy_head
        val.next = self.dummy_head.next
        self.dummy_head.next = val

    def _remove_from_cache(self, val):
        val.prev.next = val.next
        val.next.prev = val.prev

    def _remove_from_end(self):
        prev = self.end.prev
        del self.cache[prev.key]
        self.capacity += 1
        self._remove_from_cache(prev)

    def get(self, key: int) -> int:
        if val := self.cache.get(key):
            self._remove_from_cache(val)
            self._update_dummy_head(val)
            return val.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if val := self.cache.get(key):
            self._remove_from_cache(val)
            self._update_dummy_head(val)
            val.val = value
        else:
            if self.capacity == 0:
                self._remove_from_end()
            self.capacity -= 1
            val = ListNode(val=value, key=key)
            self._update_dummy_head(val)
            self.cache[key] = val


def lru_cache(capacity=128):
    cache = LRUCache(capacity)

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
