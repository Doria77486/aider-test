# aider-test

A small Python repository for testing [aider](https://aider.chat/).

## Purpose

This repo is for experiments only; it is not a real project. It intentionally
contains small files that make edit behavior easy to observe:

- Small functions with clear boundaries, useful for verifying the `diff` and
  `whole` edit formats
- An unused import and some style issues, useful for triggering lint
- A minimal CLI entry point, useful for end-to-end change tests

## Layout

```
aider-test/
├── main.py        # CLI entry point
├── calc.py        # arithmetic operations
├── utils.py       # input parsing and formatting
└── README.md
```

## Usage

```bash
python3 main.py add 1 2
python3 main.py div 10 4
python3 main.py pow 2 10
```

## Known issues

- `div` in `calc.py` does not handle division by zero
- `parse_number` in `utils.py` does not support negative numbers
- `main.py` lacks argument validation beyond basic checks

These are left in place on purpose, for aider to fix.

## Note

The `.aider.conf.yml` in this repo configures `lint-cmd`, which runs once for
every Python file successfully edited inside aider. This exists to test
config-driven command execution. **It is not how a normal project should be
configured.**
