"""Imptementation of linked list using classes in Python 3."""
# TODO: Element of linked list must contain links to previos and next element
# TODO: Get element by "[]" sugar
# TODO: Pop element with delition
# TODO: Get element by index wout delition
# import types


class LinkedList():
    """Class that implements linked list mechanism."""

    def __init__(
        self: 'LinkedList',
        elements_type: type
    ):
        """Initialize linked list with one attribute @elements_type.

        Arrtibutes:
        -----------
        @elements_type: type of any element in Linked List container.
        Adding elements with different type will raise TypeError
        """
        if not isinstance(elements_type, type):
            raise TypeError(f'Argument [elements_type] must be {type}')

        self._item_type = elements_type
        self._first_element = None
        self._last_element = None
        self._count_elements = 0

    def get_type(self: 'LinkedList') -> type:
        """Get information about types of elements."""
        return self._item_type

    def push(self: 'LinkedList', element):
        """Push element to the end of LinkedList."""
        if not isinstance(element, self._item_type):
            raise TypeError(f'Argument [element] must be {self._item_type}')

        if self._last_element is None:
            self._first_element = LinkedListItem(
                value=element,
                next=None,
                index=0)
            self._last_element = self._first_element
            self._first_element.next = self._last_element
        else:
            self._last_element.next = LinkedListItem(
                value=element,
                next=None,
                index=self._last_element.index + 1)
            self._last_element = self._last_element.next

        self._count_elements += 1

    def get_last(self):
        return self._last_element

    def get_first(self):
        return self._first_element

    def get_by_index(
        self: 'LinkedList',
        index: int
    ) -> 'LinkedListItem':
        if not isinstance(index, int):
            raise TypeError(f'Argument [index] must be {int}')

        if index < 0:
            raise ValueError('Argument [index] must be >= 0')

        temp = self._first_element
        while temp is not None:
            if temp.index == index:
                return temp
            temp = temp.next

        raise IndexError('Index out of range')

    def get_all_list(self):
        result = list()
        temp_link = self._first_element
        while temp_link is not None:
            result.append(temp_link)
            if temp_link == temp_link.next:
                break
            temp_link = temp_link.next

        return result


class LinkedListItem():
    """Helper class to define LinkedList."""

    def __init__(self: 'LinkedListItem', value, next, index):
        self.value = value
        self.next = next
        self.index = index

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        if not self.index:
            return f'(Index: {self.index}, Value: {self.value})'
        return f'\n(Index: {self.index}, Value: {self.value})'


if __name__ == '__main__':
    var = LinkedList(int)
    print(var.get_type())

    var.push(1)
    print(var.get_first(), var.get_last())
    print(var.get_all_list())

    var.push(2)
    print(var.get_first(), var.get_last())
    print(var.get_all_list())

    var.push(3)
    print(var.get_first(), var.get_last())
    print(var.get_all_list())

    var.push(4)
    print(var.get_first(), var.get_last())

    print(var.get_all_list())

    for i in range(3, -5, -1):
        print(var.get_by_index(i))
