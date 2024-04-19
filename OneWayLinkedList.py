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
        head_value = self._head.value if self._head else None
        tail_value = self._tail.value if self._tail else None
        return f"{head_value}->{tail_value}"

    def __iter__(self) -> 'OneWayLinkedList':
        self._current = self._head
        return self

    def __next__(self) -> Any:
        if not self._current:
            raise StopIteration
        value = self._current.value
        self._current = self._current.next_node
        return value

    def insert_node(self, before: Any, after: Any) -> None:
        """
        将新元素插入到指定节点之后
        :param before: 指定节点
        :param after: 要插入的节点
        :return:
        """
        new_node = OneWayLinkedListNode(after)
        current_node = self._head

        while current_node:
            if current_node.value == before:
                new_node.next_node = current_node.next_node
                current_node.next_node = new_node
                return
            current_node = current_node.next_node
        return

    def _append_node(self, new_node: OneWayLinkedListNode, direction: str = 'tail') -> None:
        """
        插入新节点至链表内
        :param new_node: 新节点
        :param direction:
                    'head': 插入至链表头部
                    'tail': 插入至链表末尾
        :return:
        """
        if self._length == 0:
            self._head = new_node
            self._tail = new_node
        else:
            if direction == 'tail':
                tail = self._tail
                tail.next_node, self._tail = new_node, new_node
            else:
                head = self._head
                new_node.next_node, self._head = head, new_node

        self._length += 1

    def tail_append_node(self, value: Any) -> None:
        """
        将新元素插入到链表的末尾，成为新的最后一个元素。
        :param value: 新元素
        :return:
        """
        new_node = OneWayLinkedListNode(value)
        self._append_node(new_node, direction='tail')

    def head_append_node(self, value: Any) -> None:
        """
        将新元素插入到链表的头部，使其成为新的第一个元素。
        :param value: 新元素
        :return:
        """
        new_node = OneWayLinkedListNode(value)
        self._append_node(new_node, direction='head')

    def find_node(self, value: Any) -> OneWayLinkedListNode | None:
        """
        根据给定的数值查找链表中的特定元素。
        :param value: 指定元素
        :return: OneWayLinkedListNode | None
        """
        current_node = self._head
        while current_node:
            if current_node.value == value:
                return current_node
            current_node = current_node.next_node
        return None

    def remove_node(self, value: Any) -> OneWayLinkedListNode | None:
        """
        根据给定的元素值删除节点。
        :param value: 指定元素
        :return: OneWayLinkedListNode | None
        """
        current_node, previous_node = self._head, None

        while current_node:
            if current_node.value == value:
                if previous_node is None:
                    self._head, current_node.next_node = current_node.next_node, None
                else:
                    previous_node.next_node, current_node.next_node = current_node.next_node, None
                self._length -= 1
                return current_node
            previous_node, current_node = current_node, current_node.next_node

        return None

    def head_remove(self) -> OneWayLinkedListNode | None:
        """
        删除链表的第一个元素。
        :return:
        """
        return self.remove_node(self._head.value)

    def tail_remove(self) -> OneWayLinkedListNode | None:
        """
        删除链表的最后一个元素。
        :return:
        """
        return self.remove_node(self._tail.value)

    def clear(self) -> None:
        """
        删除链表中的所有元素，使链表为空。
        :return:
        """
        current = self._head
        while current:
            next_node = current.next_node
            current.next_node, current = None, next_node

        self._head = None
        self._tail = None
        self._length = 0

        return
