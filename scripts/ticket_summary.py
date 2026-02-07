import argparse
import csv
from collections import Counter


def main():
    parser = argparse.ArgumentParser(description="Summarize tickets by status and owner")
    parser.add_argument("--input", required=True, help="Path to CSV file")
    args = parser.parse_args()

    status_counter = Counter()
    owner_counter = Counter()

    with open(args.input, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            status_counter[row.get("status", "unknown")] += 1
            owner_counter[row.get("owner", "unknown")] += 1

    print("Ticket count by status:")
    for key, value in sorted(status_counter.items()):
        print(f"- {key}: {value}")

    print("\nTicket count by owner:")
    for key, value in sorted(owner_counter.items()):
        print(f"- {key}: {value}")


if __name__ == "__main__":
    main()
