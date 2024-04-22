from typing import Any, Iterable


class CirculateLinkedListNode:
    def __init__(
            self,
            value: Any,
            next_node: 'CirculateLinkedListNode' = None,
    ) -> None:
        self.value = value
        self.next_node = next_node

    def __str__(self) -> str:
        return f'CirculateLinkedListNode: <({self.value} -> {self.next_node})>'


class CirculateLinkedList:
    def __init__(self, iterable: Iterable[Any] = ()) -> None:
        self.head: CirculateLinkedListNode | None = None
        self._length: int = 0

    def __len__(self) -> int:
        return self._length

    def __str__(self):
        head_value = self.head.value if self.head else None
        tail_value = self._get_tail_node().value if self._get_tail_node() else None
        return f'CirculateLinkedList: <({head_value} -> {tail_value})>'

    def _get_tail_node(self) -> CirculateLinkedListNode | None:
        if self.head is None:
            return None
        current_node = self.head
        while current_node:
            if hex(id(current_node.next_node)) == hex(id(self.head)):
                return current_node

            current_node = current_node.next_node

    def __iter__(self) -> 'CirculateLinkedList':
        self._current_node = self.head
        return self

    def __next__(self) -> Any:
        if self._current_node is None:
            raise StopIteration('CirculateLinkedList is empty')

        value = self._current_node.value
        self._current_node = self._current_node.next_node
        return value

    def _append(self, value: Any, position: str) -> None:
        new_node = CirculateLinkedListNode(value)
        if self.head is None:
            self.head = new_node
            self.head.next_node = self.head
            self._length += 1
            return

        tail_node = self._get_tail_node()

        if position == 'tail':
            tail_node.next_node, new_node.next_node = new_node, self.head

        elif position == 'head':
            new_node.next_node = self.head
            self.head = new_node
            tail_node.next_node = new_node
        self._length += 1

    def _pop(self, position: str) -> CirculateLinkedListNode:
        if position not in ["head", "tail"]:
            raise ValueError(f'not support {position}')

        head_node = self.head
        if head_node is None:
            raise IndexError(f"pop from an empty linked list")
        tail_node = self._get_tail_node()

        if position == 'head':
            tail_node.next_node = self.head = head_node.next_node
            head_node.next_node = None
            pop_node = head_node
        elif position == 'tail':
            ...
        else:
            ...
        self._length -= 1
        return pop_node

    def append(self, value: Any) -> None:
        self._append(value, position='tail')

    def appendleft(self, value: Any) -> None:
        self._append(value, position='head')

    def popleft(self) -> CirculateLinkedListNode:
        return self._pop(position='head')
