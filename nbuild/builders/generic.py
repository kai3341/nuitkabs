import sys
import subprocess


class NGenericBuilder:
    __entry_keys__ = (
        'follow-import-to',
        'nofollow-import-to',
    )

    def __init__(self, config, current_name):
        self.config = config
        self.current_name = current_name

    def run(self):
        args = self.args()
        subprocess.run(args)

    @classmethod
    def execute(cls, config, current_name):
        self = cls(config, current_name)
        self.run()

    def args_generic_iter(self):
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

    def args(self):
        self.prepare_data()
        args = self.args_iter()
        return tuple(args)

    def args_handler__dict_iter(self, entry):
        for key, values in entry.items():
            for value in values:
                yield '--%s=%s' % (key, value)

    def args_handler__string_iter(self, entry):
        yield '--%s' % entry

    args_handler_switch = {
        str: args_handler__string_iter,
        dict: args_handler__dict_iter,
    }

    def args_iter(self):
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
