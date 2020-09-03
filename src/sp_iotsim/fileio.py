import typing as T
import typing.io as Ti
import sys


def handle_packet(data: T.Union[str, bytes], f: Ti.TextIO):
    if isinstance(data, str):
        print(data)
        f.write(data + "\n")
    else:
        print(
            "unexpected binary data: ", data.decode("utf8", errors="ignore"), file=sys.stderr,
        )
