from typing import Any


class OneWayLinkedListNode:
    def __init__(
            self, value: Any,
            next_node: 'OneWayLinkedListNode' = None,
    ):
        self._value = value
        self._next_node = next_node

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: Any):
        self._value = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, next_node: 'OneWayLinkedListNode'):
        self._next_node = next_node

    def __str__(self):
        return f"{self.value}->{self.next_node}"


class OneWayLinkedList:
    def __init__(
            self,
            head: OneWayLinkedListNode | None = None,
            tail: OneWayLinkedListNode | None = None,
    ) -> None:
        self._head = head
        self._tail = tail
        self._length = 0

    def __len__(self) -> int:
        return self._length

    def __str__(self) -> str:
        return f"{self._head.value}->{self._tail.value}"

    def __iter__(self) -> 'OneWayLinkedList':
        self._current = self._head
        return self

    def __next__(self) -> Any:
        if not self._current:
            raise StopIteration
        value = self._current.value
        self._current = self._current.next_node
        return value

    def _append_node(self, node: OneWayLinkedListNode, direction: str = 'tail') -> None:
        if self._length == 0:
            self._head = node
            self._tail = node
        else:
            if direction == 'tail':
                tail = self._tail
                tail.next_node, self._tail = node, node
            else:
                head = self._head
                node.next_node, self._head = head, node

        self._length += 1

    def tail_append_node(self, value: Any) -> None:
        new_node = OneWayLinkedListNode(value)
        self._append_node(new_node, direction='tail')

    def head_append_node(self, value: Any) -> None:
        new_node = OneWayLinkedListNode(value)
        self._append_node(new_node, direction='head')

    def find_node(self, value: Any) -> Any:
        current_node = self._head
        while current_node:
            if current_node.value == value:
                return current_node
            current_node = current_node.next_node
        return None

    def remove_node(self, value: Any) -> None:
        ...


def oneway_linked_list():
    return OneWayLinkedList()


if __name__ == '__main__':
    linked_list = oneway_linked_list()
    linked_list.tail_append_node(1)
    linked_list.tail_append_node(2)
    linked_list.head_append_node(0)
    linked_list.tail_append_node(3)
    print(linked_list)
    for node in linked_list:
        print(node)
    print(linked_list.find_node(3))
    print(linked_list.find_node(4))
