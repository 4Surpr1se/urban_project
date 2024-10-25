# Реализует полноценный кэш с удалением ненужных элементов из памяти


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


# Могут встречаться и такие решения. Они реализуют просто сам класс, однако идее lru кэша не соответствуют,
# принимаемое решение, но можно в ос ученику на это указать,


from collections import OrderedDict


class LRUCache:
    __slots__ = ('data', 'capacity')

    def __init__(self, capacity: int):
        self.data = OrderedDict()
        self.capacity: int = capacity

    def get(self, key: int) -> int:
        return -1 if key not in self.data else self.data.setdefault(key, self.data.pop(key))

    def put(self, key: int, value: int) -> None:
        try:
            self.data.move_to_end(key)
            self.data[key] = value
        except KeyError:
            self.data[key] = value
            if len(self.data) > self.capacity:
                self.data.popitem(last=False)
