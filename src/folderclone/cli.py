"""Command-line interface for FolderClone."""

import argparse
from .core import sync_directories


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Synchronise directory structures with FolderClone."
    )
    parser.add_argument("src", help="Source directory.")
    parser.add_argument("dst", help="Destination directory.")
    parser.add_argument(
        "--dry-run", action="store_true", help="Show what would happen, but don't make changes."
    )
    args = parser.parse_args()

    sync_directories(args.src, args.dst, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
