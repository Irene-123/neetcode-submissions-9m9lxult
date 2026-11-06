class Node:
    def __init__(self, key, value):
        self.key = key 
        self.value = value
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key: int, value: int) -> None:
        hashed_key = self._hash(key)
        head = self.buckets[hashed_key]

        while head:
            if head.key == key:
                head.value = value
                return
            head = head.next

        node = Node(key, value)
        node.next = self.buckets[hashed_key]
        self.buckets[hashed_key] = node
        self.size += 1

        if self.size / self.capacity >= 0.5:
            self.resize()


    def get(self, expected_key: int) -> int:
        hashed_key = self._hash(expected_key)
        if self.buckets[hashed_key] == None:
            return -1

        head = self.buckets[hashed_key]
        while head != None:
            key, value = head.key, head.value
            if key == expected_key:
                return value 
            head = head.next

        return -1

    def remove(self, key: int) -> bool:
        # Key not present, key in the middle, key at the head

        hashed_key = self._hash(key)
        curr = self.buckets[hashed_key]
        prev = None

        while curr:
            if curr.key == key:
                if prev == None:
                    self.buckets[hashed_key] = curr.next
                else:
                    prev.next = curr.next
                self.size -= 1
                return True

            prev = curr
            curr = curr.next 
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        old_buckets = self.buckets.copy()
        self.capacity*= 2
        self.buckets = [None]*self.capacity

        for head in old_buckets:
            curr = head 

            while curr:
                next_node = curr.next 
                new_index = self._hash(curr.key)

                curr.next = self.buckets[new_index]
                self.buckets[new_index] = curr

                curr = next_node