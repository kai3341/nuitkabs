from .generic import NGenericBuilder


class NModuleBuilder(NGenericBuilder):
    def prepare_data(self):
        modules = self.config['modules']
        self.other_modules = modules.copy()
        self.current_entry = self.other_modules.pop(self.current_name)

    def args_generic_iter(self):
        yield from super().args_generic_iter()
        yield '--module'

