from typing import Any


class TwoWayLinkedListNode:
    def __init__(self, value: Any, prev_node=None, next_node=None):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node

    def __str__(self):
        return f"node: {self.value}"


class TwoWayLinkedList:
    def __init__(self, head: TwoWayLinkedListNode | None = None, tail: TwoWayLinkedListNode | None = None):
        self._head = head
        self._tail = tail
        self._length = 0
        self._current: TwoWayLinkedListNode | None = None

    def __len__(self):
        return self._length

    def __iter__(self):
        self._current = self._head
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        value = self._current.value
        self._current = self._current.next_node
        return value

    def __reversed__(self):
        current = self._tail
        while current:
            yield current.value
            current = current.prev_node

    def _append_node(self, node: TwoWayLinkedListNode, position: str = 'tail') -> None:
        """
        往链表内添加数据
        :param node: 链表节点
        :param position:
                    head: 往链表头部添加数据
                    tail: 往链表尾部添加数据
        :return:
        """
        if self._length == 0:
            self._head = node
            self._tail = node
        else:
            if position == 'tail':
                tail = self._tail
                tail.next_node, self._tail, self._tail.prev_node = node, node, tail
            else:
                head = self._head
                head.prev_node, self._head, self._head.next_node = node, node, head
        self._length += 1

    def add_head_node(self, value: Any) -> None:
        """
        在链表头部添加数据
        :param value:
        :return:
        """
        node = TwoWayLinkedListNode(value)

        self._append_node(node, 'head')

    def add_tail_node(self, value: Any) -> None:
        """
        在链表尾部添加数据
        :param value:
        :return:
        """
        node = TwoWayLinkedListNode(value)

        self._append_node(node, 'tail')

    def _remove_node(self, position: str = 'tail') -> None:
        """
        从链表内移除数据
        :param position:
                    head: 从头部移除;
                    tail: 从尾部移除;
        :return:
        """
        if self._length == 0:
            raise IndexError("out of range")

        if self._length == 1:
            self._head, self._tail, self._length = None, None, 0
            return

        if position == 'tail':
            tail_prev, tail_prev.next_node = self._tail.prev_node, None
            self._tail = tail_prev
        else:
            head_next, head_next.prev_node = self._head.next_node, None
            self._head = head_next

        self._length -= 1

    def remove_tail_node(self) -> None:
        """
        从链表尾部移除数据
        :param :
        :return:
        """
        self._remove_node('tail')

    def remove_head_node(self) -> None:
        """
        从链表头部移除数据
        :param :
        :return:
        """
        self._remove_node('head')

    def remove_node(self, value: Any):
        """
        删除指定节点数据
        :param value:
        :return:
        """
        current = self._head
        # 从链表的头节点开始，沿着链表的 next 指针依次遍历每个节点，直到找到要删除的节点。
        while current:
            # 找到要删除的节点后，更新前一个节点和后一个节点的指针，将它们连接起来。
            if current.value == value:
                # 如果要删除的节点是头节点，需要更新链表的头指针。
                if current.prev_node is None:
                    current.next_node.prev_node = None
                    self._head = current.next_node
                    return

                # 如果要删除的节点是尾节点，需要更新链表的尾指针。
                if current.next_node is None:
                    current.prev_node.next_node = None
                    self._tail = current.prev_node
                    return

                current.prev_node.next_node, current.next_node.prev_node = current.next_node, current.prev_node
                return
            current = current.next_node

        raise ValueError("value is not exist")


def init_twoway_linked_list():
    return TwoWayLinkedList()
