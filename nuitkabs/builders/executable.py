from .generic import NGenericBuilder


class NExecutableBuilder(NGenericBuilder):
    __entry_keys__ =  NGenericBuilder.__entry_keys__ + (
        'include-package-data',
        'include-data-file',
        'include-data-dir',
    )

    def prepare_data(self) -> None:
        executables = self.config['executables']
        self.other_modules = self.config['modules']
        self.current_entry = executables[self.current_name]
