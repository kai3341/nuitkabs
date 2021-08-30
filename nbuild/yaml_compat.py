from yaml import load  # noqa

try:
    from yaml import CLoader as Loader  # noqa
except ImportError:
    from yaml import Loader  # noqa
