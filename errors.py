"""Data structures errors."""


DEFAULT_TYPE_ERROR_MSG = 'Variable type error'
DEFAULT_STACK_OVERFLOW_MSG = 'Stack if full'
DEFAULT_STACK_IS_EMPTY_MGS = 'Stack is empty'


class DSTypeError(Exception):
    def __init__(
        self: 'DSTypeError',
        message: str = DEFAULT_TYPE_ERROR_MSG,
        target: str = None,
        variable_name: str = None,
        variable_need_type: type = None,
        variable_got_type: type = None
    ):
        self._message = message
        self._target = target
        self._var_name = variable_name
        self._need_type = variable_need_type,
        self._got_type = variable_got_type

    def __str__(self: 'DSTypeError') -> str:
        """Return full text message with given arguments."""
        result_message = '{target}{msg}: {var} {type}'
        _target = ''
        _var = ''
        _type = ''

        # If need and got type were given
        if not(self._need_type is None or self._got_type is None):
            _type = f'must be {self._need_type[0]} but got {self._got_type}'

        # If function name was given
        if self._target is not None:
            _target = f'[In funtcion "{self._target}"] '

        # If variable nambe was given
        if self._var_name is not None:
            _var = f'variable "{self._var_name}"'

        return result_message.format(
            target=_target,
            msg=self._message,
            var=_var,
            type=_type)


class DSStackOverflow(Exception):
    def __init__(
        self: 'DSStackOverflow',
        message: str = DEFAULT_STACK_OVERFLOW_MSG,
        target: str = None
    ):
        self._message = message
        self._target = target

    def __str__(self: 'DSStackOverflow'):
        if self._target is not None:
            return '[In function "{target}"]: {msg}'.format(
                target=self._target, msg=self._message)
        return self._message


class DSStackIsEmpty(Exception):
    def __init__(
        self: 'DSStackIsEmpty',
        message: str = DEFAULT_STACK_IS_EMPTY_MGS,
        target: str = None
    ):
        self._message = message
        self._target = target

    def __str__(self: 'DSStackIsEmpty') -> str:
        if self._target is not None:
            return '[In function "{target}"]: {msg}'.format(
                target=self._target, msg=self._message)
        return self._message
