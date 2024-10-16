from typing import Optional, Dict

class ListNode:
    """A node in a doubly linked list."""
    def __init__(self, key: int = None, value: int = None):
        self.key: int = key
        self.value: int = value
        self.prev: Optional[ListNode] = None
        self.next: Optional[ListNode] = None
    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(key={self.key}, value={self.value})"

class LRUCache(dict):
    """LRU Cache implemented using dict + doubly linked list."""
    def __init__(self, capacity: int):
        super().__init__()
        self.capacity: int = capacity
        self.head: ListNode = ListNode()  # Dummy head
        self.tail: ListNode = ListNode()  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: ListNode) -> None:
        """Remove a node from the linked list."""
        prev_node, next_node = node.prev, node.next
        if prev_node and next_node:
            prev_node.next = next_node
            next_node.prev = prev_node

    def _add_to_tail(self, node: ListNode) -> None:
        """Add a node right before the tail (most recently used)."""
        prev_tail: ListNode = self.tail.prev
        if prev_tail:
            prev_tail.next = node
            node.prev = prev_tail
            node.next = self.tail
            self.tail.prev = node

    def get(self, key: int) -> int:
        """Get the value of a key and mark it as recently used."""
        if key not in self:
            return -1
        node = self[key]
        # Move the accessed node to the end
        self._remove(node)
        self._add_to_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """Insert/update a key-value pair in the cache and mark it as recently used."""
        if key in self:
            # Update the value and move it to the end
            node = self[key]
            node.value = value
            self._remove(node)
            self._add_to_tail(node)
        else:
            if len(self) >= self.capacity:
                # Remove the least recently used node (head's next)
                lru_node = self.head.next
                if lru_node:
                    self._remove(lru_node)
                    del self[lru_node.key]
            # Create a new node and add it to the dict and linked list
            new_node = ListNode(key, value)
            self[key] = new_node
            self._add_to_tail(new_node)

    def delete(self, key: int) -> bool:
        """Remove a specific key from the cache. Returns True if successful."""
        if key not in self:
            return False
        node = self[key]
        self._remove(node)
        del self[key]
        return True

    def reset(self) -> None:
        """Clear the entire cache."""
        super().clear()
        self.head.next = self.tail
        self.tail.prev = self.head
