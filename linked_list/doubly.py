import copy
from typing import Any, Iterable


class TwoWayLinkedListNode:
    def __init__(
            self, value: Any,
            prev_node: 'TwoWayLinkedListNode' = None,
            next_node: 'TwoWayLinkedListNode' = None,
    ):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node

    def __str__(self):
        return f"DoublyLinkedListNode: <({hex(id(self.prev_node))} -> {self.value} -> {hex(id(self.next_node))})>"


class TwoWayLinkedList:
    def __init__(
            self,
            iterable: Iterable[Any] = (),
    ):
        self.head: TwoWayLinkedListNode | None = None
        self.tail: TwoWayLinkedListNode | None = None
        self._length: int = 0
        self._makeup_linkedlist(iterable)

    def _makeup_linkedlist(self, iterable: Iterable[Any]) -> None:
        for item in iterable:
            new_node = TwoWayLinkedListNode(item)
            self._append_node(new_node, 'tail')

    def __str__(self):
        head_value = self.head.value if self.head else None
        tail_value = self.tail.value if self.tail else None
        return f"DoublyLinkedList: <({head_value} -> {tail_value})>"

    def __len__(self):
        return self._length

    def __iter__(self):
        self._current = self.head
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        value = self._current.value
        self._current = self._current.next_node
        return value

    def __reversed__(self):
        current = self.tail
        while current:
            yield current.value
            current = current.prev_node

    def _append_node(self, new_node: TwoWayLinkedListNode, position: str = 'tail') -> None:
        """
        往链表内添加数据
        :param new_node: 链表节点
        :param position:
                    head: 往链表头部添加数据
                    tail: 往链表尾部添加数据
        :return:
        """
        if self._length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            if position == 'tail':
                tail = self.tail
                tail.next_node, self.tail, self.tail.prev_node = new_node, new_node, tail
            else:
                head = self.head
                head.prev_node, self.head, self.head.next_node = new_node, new_node, head
        self._length += 1

    def appendleft(self, value: Any) -> None:
        """
        在链表头部添加数据
        :param value:
        :return:
        """
        new_node = TwoWayLinkedListNode(value)

        self._append_node(new_node, 'head')

    def append(self, value: Any) -> None:
        """
        在链表尾部添加数据
        :param value:
        :return:
        """
        new_node = TwoWayLinkedListNode(value)

        self._append_node(new_node, 'tail')

    def extend(self, linkedlist: 'TwoWayLinkedList') -> None:
        """
        扩展linked list的右侧，通过添加linkedlist参数中的元素。
        :param linkedlist: linked list
        :return:
        """
        linkedList = copy.deepcopy(linkedlist)
        self.tail.next_node = linkedList.head
        linkedList.head.prev_node = self.tail
        self.tail = linkedList.tail
        self._length += len(linkedList)

    def extendleft(self, linkedlist: 'TwoWayLinkedList') -> None:
        """
        扩展linked list的左侧，通过添加linkedlist参数中的元素。
        :param linkedlist: linked list
        :return:
        """
        linkedList = copy.deepcopy(linkedlist)
        self.head.prev_node = linkedList.tail
        linkedList.tail.next_node = self.head
        self.head = linkedList.head
        self._length += len(linkedList)

    def insert(self, before: Any, after: Any) -> None:
        """
        在位置before插入after。
        :param before:
        :param after:
        :return:
        """
        current_node = self.head
        while current_node:
            if self.tail.value == before:
                self.append(after)
                return
            if current_node.value == before:
                new_node = TwoWayLinkedListNode(after)
                # 新node的下一个node -> 当前node的下一个node | 新node的上一个node -> 当前node
                new_node.next_node, new_node.prev_node = current_node.next_node, current_node
                # 当前node的下一个node的上一个node -> 新node | 当前node的下一个node -> 新node
                current_node.next_node.prev_node, current_node.next_node = new_node, new_node
                self._length += 1
                return
            current_node = current_node.next_node
        raise IndexError(f"{before} not in linked list")

    def _remove_node(self, position: str, current: TwoWayLinkedListNode | None = None) -> None:
        """
        从链表内移除数据
        :param position:
                    left: 从头部移除;
                    right: 从尾部移除;
                    position: 指定位置移除;
        :param current: 指定位置节点
        :return:
        """
        if self._length == 0:
            raise IndexError("pop from an empty linked list")

        if self._length == 1:
            self.head, self.tail, self._length = None, None, 0
            return

        if position == 'right':
            tail_prev, tail_prev.next_node = self.tail.prev_node, None
            self.tail = tail_prev
        elif position == 'left':
            head_next, head_next.prev_node = self.head.next_node, None
            self.head = head_next
        else:
            current.prev_node.next_node, current.next_node.prev_node = current.next_node, current.prev_node
        self._length -= 1

    def pop(self) -> TwoWayLinkedListNode:
        """
        从链表尾部移除数据
        :param :
        :return:
        """
        pop_node = self.tail
        self._remove_node('right')
        return pop_node

    def popleft(self) -> TwoWayLinkedListNode:
        """
        从链表头部移除数据
        :param :
        :return:
        """
        pop_node = self.head
        self._remove_node('left')
        return pop_node

    def remove(self, value: Any) -> None:
        """
        移除找到的第一个 value。
        :param value:
        :return:
        """
        current = self.head
        # 从链表的头节点开始，沿着链表的 next 指针依次遍历每个节点，直到找到要删除的节点。
        while current:
            # 找到要删除的节点后，更新前一个节点和后一个节点的指针，将它们连接起来。
            if current.value == value:
                # 如果要删除的节点是头节点，需要更新链表的头指针。
                if current.prev_node is None:
                    self._remove_node('left')
                # 如果要删除的节点是尾节点，需要更新链表的尾指针。
                elif current.next_node is None:
                    self._remove_node('right')
                else:
                    self._remove_node('position', current)

                return
            current = current.next_node

        raise ValueError(f"{value} is not in linked list")

    def clear(self) -> None:
        """
        清空双向链表内的元素
        :return:
        """
        current_node = self.head
        while current_node:
            next_node = current_node.next_node
            current_node.prev_node, current_node.next_node = None, None
            current_node = next_node

        self.head, self.tail, self._length = None, None, 0

    def find(self, value: Any) -> TwoWayLinkedListNode | None:
        """
        根据给定的数值查找链表中的特定元素。
        :param value: 指定元素
        :return: TwoWayLinkedListNode | None
        """
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return current_node
            current_node = current_node.next_node
        return
