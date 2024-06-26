from copy import deepcopy
from typing import Any, Iterable


class OneWayLinkedListNode:
    def __init__(
            self,
            value: Any,
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
        return f"SinglyLinkedList: <{self.value} -> {hex(id(self.next_node))}>"


class OneWayLinkedList:
    def __init__(
            self,
            iterable: Iterable[Any] = ()
    ) -> None:
        self._head: OneWayLinkedListNode | None = None
        self._length: int = 0
        self._makeup_linkedlist(iterable)

    def _makeup_linkedlist(self, iterable: Iterable[Any]) -> None:
        for value in iterable:
            new_node = OneWayLinkedListNode(value)
            self._append(new_node, 'tail')

    def __len__(self) -> int:
        return self._length

    def __str__(self) -> str:
        if self._head is None:
            return f"SinglyLinkedList: <({None} -> {None})>"

        return f"SinglyLinkedList: <({self._head.value} -> {self._get_tail_node().value})>"

    def __iter__(self) -> 'OneWayLinkedList':
        self._current = self._head
        return self

    def __next__(self) -> Any:
        if not self._current:
            del self._current
            raise StopIteration
        value = self._current.value
        self._current = self._current.next_node
        return value

    def _get_tail_node(self) -> OneWayLinkedListNode:
        """
        获取链表尾部
        :return:
        """
        current_node = self._head
        tail_node = None
        while current_node:
            if current_node.next_node is None:
                tail_node = current_node
            current_node = current_node.next_node
        return tail_node

    def _append(self, new_node: OneWayLinkedListNode, direction: str) -> None:
        """
        插入新节点至链表内
        :param new_node: 新节点
        :param direction:
        head: 插入至链表头部 tail: 插入至链表尾部
        :return:
        """
        if direction not in ['tail', 'head']:
            raise ValueError(f'not support {direction}')

        if self._head is None:
            self._head = new_node
        else:
            if direction == 'tail':
                tail_node = self._get_tail_node()
                tail_node.next_node = new_node
            else:
                old_head_node = self._head
                self._head, self._head.next_node = new_node, old_head_node

        self._length += 1

    def insert(self, before: Any, after: Any) -> None:
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
                new_node.next_node, current_node.next_node = current_node.next_node, new_node
                self._length += 1
                return
            current_node = current_node.next_node
        raise IndexError(f"{before} not in linked list")

    def append(self, value: Any) -> None:
        """
        将新元素插入到链表的末尾，成为新的最后一个元素。
        :param value: 新元素
        :return:
        """
        new_node = OneWayLinkedListNode(value)
        self._append(new_node, direction='tail')

    def appendleft(self, value: Any) -> None:
        """
        将新元素插入到链表的头部，使其成为新的第一个元素。
        :param value: 新元素
        :return:
        """
        new_node = OneWayLinkedListNode(value)
        self._append(new_node, direction='head')

    def find(self, value: Any) -> OneWayLinkedListNode | None:
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

    def _remove(self, value: Any) -> OneWayLinkedListNode:
        """
        根据给定的元素值删除节点。
        :param value: 指定元素
        :return: OneWayLinkedListNode
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

        raise IndexError(f"{value} not in linked list")

    def remove(self, value: Any) -> None:
        self._remove(value)

    def _pop(self, direction: str) -> OneWayLinkedListNode:
        """
        弹出元素
        :param direction: head: 弹出头部元素 tail: 弹出尾部元素
        :return: OneWayLinkedListNode
        """
        if direction not in ["head", "tail"]:
            raise ValueError(f'not support {direction}')

        if self._head is None:
            raise IndexError(f"pop from an empty linked list")

        current_node = self._head
        if direction == "head":
            self._head, current_node.next_node = self._head.next_node, None
        else:
            previous_node = None
            while current_node:
                if current_node.next_node is None:
                    previous_node.next_node = None
                    break
                previous_node = current_node
                current_node = current_node.next_node

        self._length -= 1
        return current_node

    def popleft(self) -> OneWayLinkedListNode:
        """
        删除链表的第一个元素。
        :return: OneWayLinkedListNode
        """
        return self._pop("head")

    def pop(self) -> OneWayLinkedListNode:
        """
        删除链表的最后一个元素。
        :return: OneWayLinkedListNode
        """
        return self._pop("tail")

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
        self._length = 0

        return

    def extend(self, linked_list: 'OneWayLinkedList') -> None:
        """
        在尾部扩展链表
        :param linked_list: 新链表
        :return:
        """
        if linked_list is None or linked_list._head is None:
            raise TypeError("'NoneType' object is not iterable")

        linkedlist_copy = deepcopy(linked_list)
        if self._head is None:
            self._head = linkedlist_copy._head
            return

        tail_node = self._get_tail_node()
        tail_node.next_node = linkedlist_copy._head
        self._length = self._length + linkedlist_copy._length

    def extendleft(self, linked_list: 'OneWayLinkedList') -> None:
        """
        在头部扩展链表
        :param linked_list: 新链表
        :return:
        """
        if linked_list is None or linked_list._head is None:
            raise TypeError("'NoneType' object is not iterable")

        linkedlist_copy = deepcopy(linked_list)
        if self._head is None:
            self._head = linkedlist_copy._head
            return

        tail_node = linkedlist_copy._get_tail_node()
        tail_node.next_node, self._head = self._head, linkedlist_copy._head
        self._length = self._length + linkedlist_copy._length
