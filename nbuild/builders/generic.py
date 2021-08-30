import sys
import subprocess
from typing import Generator, Tuple


class NGenericBuilder:
    __entry_keys__ = (
        'follow-import-to',
        'nofollow-import-to',
    )

    def __init__(self, config, current_name) -> None:
        self.config = config
        self.current_name = current_name

    def run(self) -> None:
        args = self.args()
        subprocess.run(args)

    @classmethod
    def execute(cls, config, current_name) -> None:
        self = cls(config, current_name)
        self.run()

    def args_generic_iter(self) -> Generator[str]:
        yield sys.executable
        yield '-m'
        yield 'nuitka'

        generic = self.config.get('generic')
        if not generic:
            return

        for entry in generic:
            entry_type = type(entry)
            entry_handler = self.args_handler_switch[entry_type]
            yield from entry_handler(self, entry)

        yield '--follow-imports'

    def args(self) -> Tuple[str]:
        self.prepare_data()
        args = self.args_iter()
        return tuple(args)

    def args_handler__dict_iter(self, entry) -> Generator[str]:
        for key, values in entry.items():
            for value in values:
                yield '--%s=%s' % (key, value)

    def args_handler__string_iter(self, entry) -> Generator[str]:
        yield '--%s' % entry

    args_handler_switch = {
        str: args_handler__string_iter,
        dict: args_handler__dict_iter,
    }

    def args_iter(self) -> Generator[str]:
        yield from self.args_generic_iter()

        for other_module in self.other_modules:
            yield '--nofollow-import-to=%s' % other_module

        if self.current_entry:
            for key in self.__entry_keys__:
                modules = self.current_module.get(key)

                if modules:
                    for module_name in modules:
                        yield '--%s=%s' % (key, module_name)

        yield self.current_name
