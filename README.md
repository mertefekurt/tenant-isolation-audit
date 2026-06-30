# tenant-isolation-audit

**Minimal Manual.** Review multi-tenant design notes for isolation and access-control gaps.

## Name

Multi-tenant bugs are high impact. This CLI checks design notes for missing tenant filters, shared resources, and weak tests.

## Install

`tenant-isolation-audit` accepts tenant isolation review notes or service design text in text, JSON, JSONL, or CSV form.

## Usage

```bash
python -m pip install -e ".[dev]"
tenant-isolation-audit examples/sample.txt
tenant-isolation-audit examples/sample.txt --json --fail-on medium
```

## Rules

| Rule | Severity | Meaning |
|---|---:|---|
| `missing-tenant-filter` | high | tenant filter is missing |
| `shared-resource` | medium | shared resource detected |
| `missing-access-test` | low | cross-tenant access test is missing |

## Tests

```bash
ruff check .
pytest
python -m tenant_isolation_audit --help
```

License: MIT

### Example Input

```text
query all accounts tenant_filter missing shared bucket access_test none
```

### Architecture

`cli.py` reads files, `core.py` evaluates records, and `rules.py` keeps the tenant-isolation-audit policy surface explicit.
