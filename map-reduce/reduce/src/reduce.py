# reduce.py
# Perform the `reduce` function to compute the word count for each unique word.

import sys
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


def parse(item: str) -> Tuple[str, int]:
    """
    Parse and individual item from a line of a file.
    """
    terms = item.strip().strip("(").strip(")").split(",")
    return terms[0], int(terms[1])


def reduce(ipath: str, opath: str):
    """
    Perform the `reduce` operation by combining
    each unique key in `ipath` and emitting a single
    tuple to `opath` with ('word', count).
    """
    memo = {}
    with open(ipath, "r") as ifile:
        for line in ifile:
            key, count = parse(line)
            if key in memo:
                memo[key] += count
            else:
                memo[key] = count

    with open(opath, "w") as ofile:
        for key, count in memo.items():
            ofile.write(f"({key}, {count})\n")


def main() -> int:
    ipath, opath = parse_arguments()
    try:
        reduce(ipath, opath)
    except Exception as e:
        print(f"[-] Runtime error: {e}")
        return EXIT_FAILURE

    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())
