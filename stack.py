"""Implementation of stack data structure."""
import errors
import typing
import sys


DEFAULT_STACK_OVERFLOW = 256


class Stack():
    """Data structure that implements behavior of stack."""

    def __init__(self: 'Stack', max_length: int = DEFAULT_STACK_OVERFLOW):
        """Create stack with locked length."""
        if not isinstance(max_length, int):
            raise errors.DSTypeError(
                target=sys._getframe().f_code.co_name,
                variable_name='max_length',
                variable_need_type=int,
                variable_got_type=type(max_length))

        self._max_length = max_length
        self._length = 0
        self._last_element = None

    def __str__(self: 'Stack') -> str:
        """Convert all data from stack to one string.

        --------------------------------------------
        This function doesn't delete any element from stack.
        @return type -> <str>
        """
        result = ''
        temp = self._last_element
        while temp is not None:
            result += f'{temp.data}, '
            temp = temp.prev
        return f'[{result[:-2]}]'

    def __repr__(self: 'Stack') -> str:
        """Implement built-in __repr__ function.

        ----------------------------------------
        @return type -> <str>
        """
        return self.__str__()

    def push(self: 'Stack', element) -> None:
        """Push element to stack.

        -------------------------
        @return type -> <None>
        """
        if self._length == self._max_length:
            raise errors.DSStackOverflow(
                message=f'Stack is full. Max length {self._max_length}',
                target=sys._getframe().f_code.co_name)

        temp = StackData(data=element, prev=self._last_element)
        self._last_element = temp
        self._length += 1

    def pop(self: 'Stack'):
        """Remove last element from Stack and return it's data.

        -------------------------------
        @return type -> <element_type>
        """
        if self._length == 0:
            raise errors.DSStackIsEmpty(target=sys._getframe().f_code.co_name)

        _data_t = self._last_element.data
        self._last_element = self._last_element.prev
        self._length -= 1
        return _data_t

    @property
    def length(self: 'Stack') -> int:
        """Return length of stack.

        --------------------------
        @return type -> <int>
        """
        return self._length

    @property
    def max_length(self: 'Stack') -> int:
        """Return max_length attribute of stack.

        ----------------------------------------
        @return type -> <int>
        """
        return self._max_length


class StackData:
    """Container that saves data in stack.

    Attributes:
    -----------
    @data — holds data of element in stack
    @prev — holds link to the previous element

    Properties:
    -----------
    [instance].data — return attribute data
    [instance].prev — return attribute prev

    Changing of attributes not allowed. In this case will be raised
    Attribute error

    Example:
    >>> a = StackData(5, None)
    >>> print(a.data) # 5
    >>> print(a.prev) # None
    >>> a.prev = StackData(6, None)
    AttributeError: can't ser attribute 'prev'
    >>> a.data = 10
    AttributeError: can't ser attribute 'data'
    """

    def __init__(
        self: 'StackData',
        data: typing.Any,
        prev: typing.Union['StackData', None]
    ) -> None:
        """Initialize StackData element."""
        self._data = data
        self._prev = prev

    def __str__(self: 'StackData') -> str:
        """Return data of element as string."""
        return str(self._data)

    def __repr__(self: 'StackData') -> str:
        """Call built-in methon __str__()."""
        return self.__str__()

    @property
    def data(self: 'StackData') -> typing.Any:
        """Return data of element."""
        return self._data

    @property
    def prev(self: 'StackData') -> typing.Union['StackData', None]:
        """Return link to previous node."""
        return self._prev


if __name__ == '__main__':
    a = Stack()

    for i in range(20):
        a.push(i)

    while a.length > 0:
        print(a.pop())

    x = StackData(2, None)
    x.prev = 3
