import os
import sys
from typing import List

def ls() -> List[str]:
    """List the contents of the current directory."""
    contents = []
    for path in os.listdir(os.getcwd()):
        if os.path.isfile(path):
            contents.append(f"F {path}")
        elif os.path.isdir(path):
            contents.append(f"D {path}")
        else:
            contents.append(f"U {path}")
    return contents

def main() -> int:
    contents = ls()
    with open("ls.txt", "w") as f:
        f.write('\n'.join(contents) + '\n')
    return 0

if __name__ == "__main__":
    sys.exit(main())
