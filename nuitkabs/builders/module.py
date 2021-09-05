from typing import Iterator
from .generic import NGenericBuilder


class NModuleBuilder(NGenericBuilder):
    def prepare_data(self) -> None:
        modules = self.config['modules']
        self.other_modules = modules.copy()
        self.current_entry = self.other_modules.pop(self.current_name)

    def args_generic_iter(self) -> Iterator[str]:
        yield from super().args_generic_iter()
        yield '--module'
