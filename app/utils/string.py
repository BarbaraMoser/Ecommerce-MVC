from typing import TypeVar

_STR_OR_NONE = TypeVar('_STR_OR_NONE', str, None)


class StringUtils:

    @classmethod
    def is_empty_or_is_null(cls, value: _STR_OR_NONE):
        if cls.is_none(cls, value) or cls.is_empty(cls, value):
            raise Exception('This information is mandatory.')
        return False

    def is_empty(self, value: str):
        value.replace(' ', '')
        return len(value)

    def is_none(self, value: None):
        return value is None
