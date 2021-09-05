import sys
import subprocess

from typing import Iterator, Tuple

from .arg_processor import arg_processor
from .package_finder import PackageFinder


class NGenericBuilder:
    __entry_keys__: Tuple[str, ...] = (
        'follow-import-to',
        'nofollow-import-to',
        'include-module',
        'include-package',
    )

    def __init__(self, config, current_name) -> None:
        self.config = config
        self.current_name = current_name

    def prepare_data(self) -> None:
        self.other_modules: dict
        self.current_entry: dict
        
    def run(self) -> None:
        args = self.args()
        completed = subprocess.run(args)
        returncode = completed.returncode

        if returncode != 0:
            print("NuitkaBS failed", args, file=sys.stderr)
            sys.exit(returncode)

    @classmethod
    def execute(cls, config, current_name) -> None:
        self = cls(config, current_name)
        self.run()

    def args_generic_iter(self) -> Iterator[str]:
        yield sys.executable
        yield '-m'
        yield 'nuitka'

        generic = self.config.get('generic')
        if generic:
            yield from self.args_handler___iter(generic)

    def args(self) -> Tuple[str, ...]:
        self.prepare_data()
        args = self.args_iter()
        return tuple(args)

    def args_handler___iter(self, entry) -> Iterator[str]:
        for key, value in entry.items():
            yield from arg_processor(value, key)

    def args_iter(self) -> Iterator[str]:
        # Pre-calculate file or module name
        canonical_name = PackageFinder.execute(self.current_name)

        yield from self.args_generic_iter()

        for other_module in self.other_modules:
            yield '--nofollow-import-to=%s' % other_module

        if self.current_entry:
            for key in self.__entry_keys__:
                modules = self.current_entry.get(key)

                if modules:
                    for module_name in modules:
                        yield '--%s=%s' % (key, module_name)

        yield canonical_name
