class MyHashMap:

    def __init__(self):
        self.dict = {}

    def put(self, key: int, value: int) -> None:
        self.dict[key] = value

    def get(self, key: int) -> int:
        return self.dict.get(key, -1)  # return -1 if key is not found

    def remove(self, key: int) -> None:
        return self.dict.pop(key) if key in self.dict else -1

obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)