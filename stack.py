"""Implementation of stack data structure."""
import errors
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
            result += f'{temp.get_data()}, '
            temp = temp.get_prev()
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

        _data_t = self._last_element.get_data()
        self._last_element = self._last_element.get_prev()
        self._length -= 1
        return _data_t

    def length(self: 'Stack') -> int:
        """Return length of stack.

        --------------------------
        @return type -> <int>
        """
        return self._length

    def max_length(self: 'Stack') -> int:
        """Return max_length attribute of stack.

        ----------------------------------------
        @return type -> <int>
        """
        return self._max_length


class StackData:
    def __init__(self, data, prev):
        self._data = data
        self._prev = prev

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return self.__str__()

    def get_data(self):
        return self._data

    def get_prev(self):
        return self._prev


if __name__ == '__main__':
    a = Stack()
