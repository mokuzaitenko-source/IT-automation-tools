# IT Automation Tools

I built these practical Python utilities for IT support workflows.

## Tools Included

- `scripts/ticket_summary.py`: summarize ticket counts by status/owner
- `scripts/log_filter.py`: filter logs by keyword and severity
- `scripts/bulk_rename.py`: safe batch rename helper for support files

## Quick Start

```powershell
python scripts/ticket_summary.py --input examples/tickets.csv
python scripts/log_filter.py --input examples/app.log --level ERROR --keyword timeout
python scripts/bulk_rename.py --path examples/files --find old --replace new --dry-run
```

## Why This Matters

These scripts reduce repetitive manual work and improve support response speed.

## Ownership

Original work by Alvin Tolbert.
