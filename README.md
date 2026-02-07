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

## What Each Tool Solves

- `ticket_summary.py`: converts raw ticket exports into quick status/owner counts for reporting.
- `log_filter.py`: extracts high-signal log lines by severity and keyword during incident triage.
- `bulk_rename.py`: safely previews file naming changes before applying them.

## Sample Outputs

- Ticket summary output: counts grouped by `status` and `owner`.
- Log filter output: targeted `ERROR` lines with keyword filtering.
- Bulk rename output: old name -> new name preview in `--dry-run` mode.

## Why This Matters

These scripts reduce repetitive manual work and improve support response speed during day-to-day IT operations.

## Ownership

Original work by Alvin Tolbert.
