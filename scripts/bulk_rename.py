import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Bulk rename files safely")
    parser.add_argument("--path", required=True, help="Directory path")
    parser.add_argument("--find", required=True, help="Text to find")
    parser.add_argument("--replace", required=True, help="Replacement text")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    args = parser.parse_args()

    base = Path(args.path)
    if not base.exists() or not base.is_dir():
        raise SystemExit("Invalid --path directory")

    for item in base.iterdir():
        if not item.is_file():
            continue
        new_name = item.name.replace(args.find, args.replace)
        if new_name == item.name:
            continue
        target = item.with_name(new_name)
        print(f"{item.name} -> {target.name}")
        if not args.dry_run:
            item.rename(target)


if __name__ == "__main__":
    main()
