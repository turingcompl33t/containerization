# map.py
# Map each word in an input file to a ('word', 1) pair in an output file.

import sys
import string
import argparse
from typing import Tuple

EXIT_SUCCESS = 0
EXIT_FAILURE = 1


def parse_arguments() -> Tuple[str, str]:
    """
    Parse commandline arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("ipath", type=str, help="The path to the input file.")
    parser.add_argument("opath", type=str, help="The path to the output file.")
    args = parser.parse_args()
    return args.ipath, args.opath


def map(ipath: str, opath: str):
    """
    Perform the `map` function to map each word in the
    file at `ipath` to a ('word', 1) pair in the file at `opath`.
    """
    with open(ipath, "r") as ifile, open(opath, "w") as ofile:
        for line in ifile:
            for word in line.strip().split():
                word = word.lower()
                word = word.translate(str.maketrans("", "", string.punctuation))
                ofile.write(f"({word}, 1)\n")


def main() -> int:
    ipath, opath = parse_arguments()
    try:
        map(ipath, opath)
    except Exception as e:
        print(f"[-] Runtime error: {e}")
        return EXIT_FAILURE

    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())
