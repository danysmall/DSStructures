"""Binary tree implementation."""
import typing


class BinTree:
    """Binary Tree class."""

    def __init__(self):
        self._length = 0
        self._count = 0
        self._root = None

    @property
    def length(self: 'BinTree') -> int:
        """Return max-length of the tree."""
        return self._length

    @length.setter
    def length(self: 'BinTree') -> None:
        raise AttributeError('Can\'t change attribute <length>')

    @property
    def count(self: 'BinTree') -> int:
        """Return count of elements in tree."""
        return self._count

    @count.setter
    def count(self: 'BinTree') -> None:
        raise AttributeError('Can\'t change attribute <count>')

    def add(
        self: 'BinTree',
        key: typing.Union[str, int],
        value: typing.Any
    ) -> None:
        if self._root is None:
            self._root = BinTreeNode(key=key, value=value)
            self._length += 1
            self._count += 1
            return

        _temp = self._root
        _hash = hash(key)
        _length = 0
        while True:
            if _hash > _temp.hash:
                if _temp.right is None:
                    _temp.right = BinTreeNode(key, value, parent=_temp)
                    self._count += 1
                    if _length > self._length:
                        self._length = _length
                    return
                _temp = _temp.right
                _length += 1

            elif _hash < _temp.hash:
                if _temp.left is None:
                    _temp.left = BinTreeNode(key, value, parent=_temp)
                    self._count += 1
                    if _length > self._length:
                        self._length = _length
                    return
                _temp = _temp.left
                _length += 1

            else:
                raise KeyError(f'The key "{key}" already exists')

    def print(self) -> str:
        """Return all elements of a tree."""
        return self._print(self._root)

    def _print(self, node=None) -> str:
        if node is None:
            return ''
        return f'{node} {self._print(node.right)} {self._print(node.left)}'

    def delete(self):
        pass

    def find(
        self: 'BinTree',
        key: typing.Union[int, str]
    ) -> typing.Any:
        """Find element in tree by the key.

        -----------------
        Return value of a key or None
        """
        _temp = self._root
        _hash = hash(key)

        while _temp is not None:
            if _hash > _temp.hash:
                _temp = _temp.right

            elif _hash < _temp.hash:
                _temp = _temp.left

            elif _hash == _temp.hash:
                return _temp.value

        return None

    def is_empty(self: 'BinTree') -> bool:
        """Return <True> if tree is empty."""
        return self._length <= 0


class BinTreeNode:
    """Node of binary tree.

    Attrubutes:
    -----------
    @key — value that indecates kind of "index" of the node.
    Uses in all actions with finding, getting and other .
    @value — <AnyType> object containt data.
    @left — <BinTreeNode> or <None> link to the left node.
    @right — <BinTreeNode> or <None> link to the right node.
    @parent — <BinTreeNode> or <None> link to the parent node.
    """

    def __init__(
        self: 'BinTreeNode',
        key: typing.Union[int, str],
        value: typing.Any,
        left: typing.Union['BinTreeNode', None] = None,
        right: typing.Union['BinTreeNode', None] = None,
        parent: typing.Union['BinTreeNode', None] = None
    ):
        """Initialize new node for adding to BinTree."""
        self._key = key
        self._value = value
        self._left = left
        self._right = right
        self._parent = parent

        self._hash = hash(key)

    def __str__(self: 'BinTreeNode') -> str:
        """Return node info in special string format."""
        return '(Key: {}, Value: {}, Left: {}, Right: {}, Root: {})'.format(
            self._key, self._value,
            self._left is not None,
            self._right is not None,
            self._parent is None)

    def __repr__(self: 'BinTreeNode') -> str:
        """Return node info in special string format."""
        return self.__str__()

    def is_root(self: 'BinTreeNode') -> bool:
        """Return <True> if the node has no parent else <False>."""
        return True if self._parent is None else False

    @property
    def hash(self: 'BinTreeNode') -> int:
        """Return unique int hash of the key."""
        return self._hash

    @property
    def key(self: 'BinTreeNode') -> typing.Union[int, str]:
        """Getter for the key value."""
        return self._key

    @key.setter
    def key(self: 'BinTreeNode', value: typing.Any):
        """Tree doesn't allow change key. Raise KeyError."""
        raise AttributeError('Can\'t change value of the key')

    @property
    def value(self: 'BinTreeNode') -> typing.Any:
        """Return data from attribute <value> of the Node."""
        return self._value

    @value.setter
    def value(self: 'BinTreeNode', value: typing.Any):
        """Set value of the node."""
        self._value = value

    @property
    def left(self: 'BinTreeNode') -> 'typing.Union[BinTreeNode, None]':
        """Return link to the left child of BinTreeNode."""
        return self._left

    @left.setter
    def left(self: 'BinTreeNode', node: 'typing.Union[BinTreeNode, None]'):
        """Raise exception if type on node is incorrect."""
        if not isinstance(node, BinTreeNode) or node is None:
            raise Exception('<Node> argument must be <BinTreeNode> or <None>')
        self._left = node

    @property
    def right(self: 'BinTreeNode') -> typing.Union[int, str]:
        """Return link to the right child of BinTreeNode."""
        return self._right

    @right.setter
    def right(self: 'BinTreeNode', node: 'typing.Union[BinTreeNode, None]'):
        if not isinstance(node, BinTreeNode) or node is None:
            raise Exception('<Node> argument must be <BinTreeNode> or <None>')
        self._right = node

    @property
    def parent(self: 'BinTreeNode') -> typing.Union[int, str]:
        """Return link to the parent child of BinTreeNode."""
        return self._parent

    @parent.setter
    def parent(self: 'BinTreeNode', node: 'typing.Union[BinTreeNode, None]'):
        if not isinstance(node, BinTreeNode) or node is None:
            raise Exception('<Node> argument must be <BinTreeNode> or <None>')
        self._parent = node


if __name__ == '__main__':
    a = BinTree()
    a.add('hello', 'world')
    a.add('good', 'job')
    a.add('nice', 'work')

    try:
        a.add('hello', 'new world')
    except KeyError as error:
        print(f'Error cathced.\n{error}')

    print(a.print())
    print(a.length, a.count)
    print(a.find('hello'), a.find('unknown'))
