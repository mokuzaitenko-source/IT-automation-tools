import argparse


def main():
    parser = argparse.ArgumentParser(description="Filter logs by level and keyword")
    parser.add_argument("--input", required=True, help="Path to log file")
    parser.add_argument("--level", default="", help="Log level to match (INFO/WARN/ERROR)")
    parser.add_argument("--keyword", default="", help="Keyword to match")
    args = parser.parse_args()

    level = args.level.upper().strip()
    keyword = args.keyword.lower().strip()

    with open(args.input, encoding="utf-8") as f:
        for line in f:
            line_check = line.strip()
            if level and f" {level} " not in line_check:
                continue
            if keyword and keyword not in line_check.lower():
                continue
            print(line_check)


if __name__ == "__main__":
    main()
