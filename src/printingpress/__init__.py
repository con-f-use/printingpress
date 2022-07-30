"""A dumb little package.

Printingpress is a dumb little module without much function.
"""

try:
    from . import version

    __version__ = version.version
except ImportError:
    __version__ = "unknown"

    
import logging, codecs, os


class EncodingHandler(logging.StreamHandler):
    def __init__(self, filename, mode="w", codec=None, errors="ignore"):
        """Handler that compresses messages and saves them in a file.

        DANGER! May silently loose log-messages that it can't encode!

        Possible algorithms: 'bz2', 'zip' - maybe more, see:
          - https://docs.python.org/3/library/codecs.html#binary-transforms"""
        self.filename = os.fspath(filename)
        if codec is None:
            ext = self.filename.rsplit(".", 1)[-1]
            codec = ext if ext in ("zip", "bz2") else "zip"
        stream = codecs.open(self.filename, mode=mode, encoding=codec)
        super().__init__(stream=stream)
        self._errors = errors
        self._codec = codec

    def emit(self, record):
        try:
            msg = self.format(record) + self.terminator
            stream = self.stream
            stream.write(msg.encode("ascii", errors=self._errors))
            stream.flush()
        except RecursionError:  # cPython issue 36272
            raise
        except Exception:
            if self._errors != "ignore":
                self.handleError(record)

    def close(self):
        """Closes the stream."""
        self.acquire()
        try:
            try:
                if self.stream:
                    try:
                        self.flush()
                    finally:
                        stream = self.stream
                        self.stream = None
                        if hasattr(stream, "close"):
                            stream.close()
            finally:
                super().close()
        finally:
            self.release()


def me(msg="I am printingpress!"):
    """Print a dumb message

    :param msg: dumb message to print
    """
    print(msg)
    return msg
