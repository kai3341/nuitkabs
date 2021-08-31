from functools import partial
from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


load_yaml = partial(load, Loader=Loader)
