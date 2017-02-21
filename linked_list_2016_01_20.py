"""Python 3 implementation of a linked list and a circular link list."""
import collections


class LinkedNode(object):
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList(collections.abc.Iterable):

    def __init__(self):
        self.start = None

    def insert(self, value, index=0):
        """Insert a value in the list at a specific index."""
        new_node = LinkedNode(value)
        if index == 0:
            # Special case the node to insert after does not exist.
            node = None
        else:
            # Find the node to insert after, by adding 1 to the emuration
            # index.
            for i, node in enumerate(self._iter_nodes, 1):
                if i == index:
                    break
            else:
                # We went through all indexes in list, index not in list.
                raise IndexError(index)
        self._insert_after(node, new_node)

    def append(self, value):
        """Append a value to the list."""
        new_node = LinkedNode(value)
        for node in enumerate(self._iter_nodes()):
            # Loop through all nodes to get the last one.
            pass
        self._insert_after(node, new_node)

    def _insert_after(self, node, new_node):
        """Insert a new node after the node.

        Special case for inserting at the start of the list.
        """
        if not node:
            # Special case if inserting at start of list.
            next_node = self.start
            self.start = new_node
        else:
            next_node = node.next
            node.next = new_node
        new_node.next = next_node

    def _pop_after(self, node):
        """Delete the node after this node, and return its value.

        Special case for deleting the first element.
        """
        if not node:
            # Special case pop first value.
            value = self.start.value
            self.start = self.start.next
        else:
            value = node.next.value
            node.next = node.next.next
        return value

    def pop(self, index=0):
        """Return value at index and delete it."""
        if not self.start:
            raise IndexError(index)
        if index == 0:
            node = None
        else:
            # Find the node to insert after, by adding 1 to the emuration
            # index.
            for i, node in enumerate(self._iter_nodes, 1):
                if i == index:
                    break
            else:
                # We went through all indexes in list, index not in list.
                raise IndexError(index)
        try:
            self._pop_after(node)
        except AttributeError:
            # Trying to delete the last + 1 object, which does not exist.
            raise IndexError(index)

    def _iter_nodes(self):
        """Iterate over all the nodes."""
        node = self.start
        while True:
            if node is None:
                return
            yield node
            node = node.next

    def __iter__(self):
        """Iter over all values in the list."""
        for node in self._iter_nodes():
            yield node.value

    def __repr__(self):
        """List representation."""
        return '[{}]'.format(', '.join(repr(n) for n in self))


def test_linked_list():
    # Started on testing the implementation, but not finished yet.
    l = LinkedList()
    for v in range(10):
        l.insert(v)
    assert list(l) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    l.append(1)
    assert list(l) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1]
    assert l.pop() == 9
    assert list(l) == [8, 7, 6, 5, 4, 3, 2, 1, 0, 1]
    assert l.pop(9) == 1


class CircularLinkedList(collections.abc.Iterable):

    """Circular linked list will append to the list in O(1) instead of
    the above implementation using O(2n).
    """

    def __init__(self):
        self.last = None

    def append(self, value):
        new_node = LinkedNode(value)
        self._insert_after(self.last, new_node)
        self.last = new_node

    def _insert_after(self, node, new_node):
        if not node:
            new_node.next = new_node
        else:
            new_node.next = node.next
            node.next = new_node

    def insert(self, value, index=0):
        new_node = LinkedNode(value)
        for i, node in enumerate(self._iter_nodes()):
            if i == index:
                self._insert_after(node, new_node)
        else:
            raise IndexError(index)
        if not self.last:
            # This is an empty list, set the last node as this new_node.
            self.last = new_node

    def pop(self, index=0):
        if not self.last:
            raise IndexError(index)
        if index == 0:
            node = self.last.next
            if node is self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next
            return node.value
        for i, node in enumerate(self._iter_nodes(), 1):
            if i == index:
                if node is self.last:
                    # We are trying to pop the node outside of the
                    # list, if we do not check for this we will delete
                    # the first node from the list.
                    raise IndexError
                old_node = node.next
                node.next = node.next.next
                if self.last is old_node:
                    # If we delete the last node make sure we reset the
                    # last node to the one before it.
                    self.last = node
                return old_node.value
        else:
            raise IndexError(index)

    def _iter_nodes(self):
        node = self.last
        if not node:
            # Empty list.
            return
        # By getting the next node before yielding we always start with
        # the first node.
        while True:
            node = node.next
            yield node
            if node is self.last:
                # If we yielded the last node we are done.
                return

    def __iter__(self):
        for node in self._iter_nodes():
            yield node.value

    def __repr__(self):
        return '[{}]'.format(', '.join(repr(n) for n in self))
