"""A dumb little package.

Printingpress is a dumb little module without much function.
"""

try:
    from . import version

    __version__ = version.version
except ImportError:
    __version__ = "unknown"


def me(msg="I am printingpress!"):
    """Print a dumb message

    :param msg: dumb message to print
    """
    print(msg)
    return msg
