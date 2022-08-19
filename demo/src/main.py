import sys

def main() -> int:
    with open("out.txt", "w") as f:
        f.write(f"{'a'*8}\n")
    return 0

if __name__ == "__main__":
    sys.exit(main())
