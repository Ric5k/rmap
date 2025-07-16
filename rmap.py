import argparse

from modules.color import colorize

def main():
    parser = argparse.ArgumentParser(
        description="rmap"
    )

    # --version を追加
    parser.add_argument(
        "-v", "--version",
        action="version",
        version="rmap 0.0.0"
    )

    args = parser.parse_args()


if __name__ == "__main__":
    main()

