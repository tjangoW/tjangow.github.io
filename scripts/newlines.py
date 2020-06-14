#!python3
import re
import sys
from pathlib import Path


def formatAllInFolder(folder_path: str) -> None:
    folder = Path(folder_path)
    for file in folder.glob("*.md"):
        filename = str(file.absolute())
        print("formatting <{}>".format(filename))
        formatNewlines(filename)


def formatNewlines(in_path: str) -> None:
    """
    Break lines for every sentences so that it will be easier when looking into diff
    """
    with open(in_path, "r") as f:
        tmp_s = f.read()

    new_s = re.sub(r"(\w{2,})([\.?!]+) (\w+)", r"\1\2\n\3", tmp_s)

    with open(in_path, "w") as f:
        f.write(new_s)


if __name__ == "__main__":
    formatNewlines(sys.argv[-1])
