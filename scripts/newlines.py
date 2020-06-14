#!python3
import re
import sys


def formatNewlines(in_path: str) -> None:
    """
    Break lines for every sentences so that it will be easier when looking into diff
    """
    with open(in_path, "r") as f:
        tmp_s = f.read()

    new_s = re.sub(r"(\w+)([\.?!]+) ", r"\1\2\n", tmp_s)

    with open(in_path, "w") as f:
        f.write(new_s)


if __name__ == "__main__":
    formatNewlines(sys.argv[-1])