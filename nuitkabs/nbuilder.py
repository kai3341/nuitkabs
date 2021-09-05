from os import getenv
from typing import Type

from .yaml_compat import load_yaml

from .builders import (
    NGenericBuilder,
    NModuleBuilder,
    NExecutableBuilder,
)


class NBuilder:
    default_config_name = 'nuitkabs.yaml'

    def __init__(self, **kwargs) -> None:
        self.config_name = kwargs.get('config_name', self.default_config_name)

    def load_config(self) -> None:
        with open(self.config_name) as config_stream:
            self.config = load_yaml(config_stream)

    def handle_entry(
        self, section_name: str,
        builder: Type[NGenericBuilder],
    ) -> None:

        entries = self.config.get(section_name)

        if not entries:
            return

        for entry_name in entries:
            builder.execute(
                self.config,
                entry_name,
            )

    handlers = (
        ('modules', NModuleBuilder),
        ('executables', NExecutableBuilder),
    )

    handler_dict = dict(handlers)

    def build_all(self) -> None:
        for section_name, builder in self.handlers:
            self.handle_entry(section_name, builder)

    def build_one(self, section_name) -> None:
        builder = self.handler_dict[section_name]

        entry_name = getenv('ENTRY_NAME')

        if entry_name:
            builder.execute(
                self.config,
                entry_name,
            )
        else:
            self.handle_entry(section_name, builder)

    def build(self) -> None:
        section_name = getenv('SECTION_NAME')

        if section_name:
            self.build_one(section_name)
        else:
            self.build_all()

    def main(self) -> None:
        self.load_config()
        self.build()

    @classmethod
    def execute(cls) -> None:
        self = cls()
        self.main()
