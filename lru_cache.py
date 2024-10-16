from typing import Optional, Iterator, Any, Tuple, List
from collections.abc import MutableMapping, KeysView, ValuesView, ItemsView

class ListNode:
    """A node in the doubly linked list."""
    def __init__(self, key: Any = None, value: Any = None):
        self.key: Any = key
        self.value: Any = value
        self.prev: Optional[ListNode] = None
        self.next: Optional[ListNode] = None

    def __repr__(self):
        prev_key = self.prev.key if self.prev else None
        next_key = self.next.key if self.next else None
        return f"{type(self).__name__}(key={self.key}, value={self.value}, prev={prev_key}, next={next_key})"

class LRUCache(MutableMapping):
    """LRU Cache implemented using MutableMapping"""
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.store: dict[Any, ListNode] = {}
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
        """Add a node right before the tail."""
        prev_tail = self.tail.prev
        if prev_tail:
            prev_tail.next = node
            node.prev = prev_tail
            node.next = self.tail
            self.tail.prev = node

    def __getitem__(self, key: Any) -> Any:
        """Get the value for a given key."""
        if key not in self.store:
            raise KeyError(key)
        node = self.store[key]
        # Move the accessed node to the end (most recently used)
        self._remove(node)
        self._add_to_tail(node)
        return node.value

    def __setitem__(self, key: Any, value: Any) -> None:
        """Insert or update a key-value pair."""
        if key in self.store:
            node = self.store[key]
            node.value = value
            self._remove(node)
            self._add_to_tail(node)
        else:
            if len(self.store) >= self.capacity:
                # Remove the least recently used node (head's next)
                lru_node = self.head.next
                if lru_node:
                    self._remove(lru_node)
                    del self.store[lru_node.key]
            new_node = ListNode(key, value)
            self.store[key] = new_node
            self._add_to_tail(new_node)

    def __delitem__(self, key: Any) -> None:
        """Delete a key from the cache."""
        if key not in self.store:
            raise KeyError(key)
        node = self.store.pop(key)
        self._remove(node)

    def __iter__(self) -> Iterator[Any]:
        """Iterate over the keys in the cache."""
        current = self.head.next
        while current and current != self.tail:
            yield current.key
            current = current.next

    def __len__(self) -> int:
        """Return the number of items in the cache."""
        return len(self.store)

    def __contains__(self, key: Any) -> bool:
        """Check if a key exists in the cache."""
        return key in self.store

    def reset(self) -> None:
        """Clear the entire cache."""
        self.store.clear()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _traverse(self) -> List[Tuple[Any, Any]]:
        """Helper to traverse the linked list in LRU order."""
        result = []
        current = self.head.next
        while current and current != self.tail:
            result.append((current.key, current.value))
            current = current.next
        return result

    def keys(self) -> KeysView:
        """Return a view of the cache's keys in LRU order."""
        return KeysView({key: None for key, _ in self._traverse()})

    def values(self) -> ValuesView:
        """Return a view of the cache's values in LRU order."""
        return ValuesView({key: value for key, value in self._traverse()})

    def items(self) -> ItemsView:
        """Return a view of the cache's items in LRU order."""
        return ItemsView(dict(self._traverse()))

    def __repr__(self) -> str:
        """String representation of LRUCache."""
        items = ", ".join(f"{key}: {value}" for key, value in self._traverse())
        return f"{type(self).__name__}(capacity={self.capacity}, items={{ {items} }})"
