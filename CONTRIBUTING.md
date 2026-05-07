# Contributing

Thanks for helping improve Founder AI Workflow ROI OS.

## Local setup

```bash
make install
make test
make run
```

## Contribution standards

- Keep the base workflow deterministic and offline-first.
- Do not add paid API requirements to the core path.
- Do not add private company data, secrets, or customer examples.
- Keep sample data synthetic and fictionalized.
- Keep scoring logic transparent and easy to explain.
- Add tests for behavior changes.
- Do not use emojis in documentation, code comments, issue templates, commit messages, or generated outputs.

## Pull request checklist

- Tests pass with `make test`.
- Demo outputs regenerate with `make run`.
- README stays founder-facing and practical.
- New configuration fields are documented.
- Generated files do not contain secrets or private data.
