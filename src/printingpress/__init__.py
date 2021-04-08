try:
    from . import version

    __version__ = version.version
except ImportError:
    __version__ = "unknown"


def me(msg="I am printingpress!"):
    print(msg)
    return msg
