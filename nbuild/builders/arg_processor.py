from functools import singledispatch

from typing import Iterator, Type
NoneType: Type = type(None)


@singledispatch
def arg_processor(value, key: str)-> Iterator[str]:
    raise TypeError(key, value)


@arg_processor.register(str)
def str__iter(value, key: str) -> Iterator[str]:
    yield '--%s=%s' % (key, value)


@arg_processor.register(NoneType)
def none__iter(value, key: str) -> Iterator[str]:
    yield '--%s' % key


@arg_processor.register(list)
@arg_processor.register(tuple)
def list__iter(value, key: str) -> Iterator[str]:
    for item in value:
        yield '--%s=%s' % (key, item)
