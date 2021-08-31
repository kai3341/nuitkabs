from functools import lru_cache
from sys import path as sys_path
from os import path as os_path

from typing import Optional


class PackageFinder:
    all_paths = tuple(
        path for path in ('.', *sys_path)
        if (os_path.exists(path) and os_path.isdir(path))
    )

    def __init__(self, current_name):
        self.current_name = current_name

    @classmethod
    @lru_cache(maxsize=None)
    def execute(cls, current_name) -> str:
        self = cls(current_name)
        return self.main()

    def main(self) -> str:
        self.name_parts = self.current_name.split('.')
        return self.canonical_name()

    def canonical_name(self) -> str:
        for path in self.all_paths:
            maybe_canonical_name = self.canonical_name__from_dir(path)

            if maybe_canonical_name:
                return maybe_canonical_name
        
        raise FileNotFoundError(self.current_name)

    def canonical_name__from_dir(self, current_dir: str) -> Optional[str]:
        path = os_path.join(current_dir, *self.name_parts)

        # Directory?
        if os_path.exists(path):
            if os_path.isdir(path):
                return path
        
        # File?
        file_path = path + '.py'
        if os_path.exists(file_path):
            if os_path.isfile(file_path):
                return file_path
