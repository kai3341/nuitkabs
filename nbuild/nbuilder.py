from .yaml_compat import load, Loader

from .builders import (
    NGenericBuilder,
    NModuleBuilder,
    NExecutableBuilder,
)


class NBuilder:
    default_config_name = 'nbuild.yaml'

    def __init__(self, **kwargs):
        self.config_name = kwargs.get('config_name', self.default_config_name)

    def load_config(self):
        with open(self.config_name) as config_stream:
            self.config = load(config_stream, Loader=Loader)

    def handle_entry(self, section_name: str, builder: NGenericBuilder):
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

    def build(self):
        for section_name, builder in self.handlers:
            self.handle_entry(section_name, builder)

    def main(self):
        self.load_config()
        self.build()

    @classmethod
    def execute(cls):
        self = cls()
        self.main()
