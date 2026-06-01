# Roman Numeral Converter

A Python library for converting:

- **Integer → Roman numeral**
- **Roman numeral → Integer**

This project was built using **Test-Driven Development (TDD)** with incremental development, meaningful refactors, and automated tests.

---

## Features

### Integer → Roman numeral

Examples:

```text
1 -> I
4 -> IV
9 -> IX
58 -> LVIII
1994 -> MCMXCIV
2024 -> MMXXIV
```

### Roman numeral → Integer

Examples:

```text
I -> 1
IV -> 4
IX -> 9
LVIII -> 58
MCMXCIV -> 1994
MMXXIV -> 2024
```

---

## Roman Numeral Rules

### Base symbols

| Symbol | Value |
|--------|------:|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

### Subtractive notation

Roman numerals use subtractive notation in specific cases:

| Roman | Value |
|--------|------:|
| IV | 4 |
| IX | 9 |
| XL | 40 |
| XC | 90 |
| CD | 400 |
| CM | 900 |

---

## Project Structure

```text
SecondChallenge/
│
├── src/
│   └── roman_converter/
│       ├── __init__.py
│       └── converter.py
│
├── tests/
│   └── test_converter.py
│
├── main.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.11+

---

## Setup

Create virtual environment:

### Windows (Git Bash)

```bash
python -m venv .venv
source .venv/Scripts/activate
```

### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running Tests

Execute all tests:

```bash
pytest
```

---

## Test Coverage

Run coverage:

```bash
pytest --cov=src
```

Detailed report:

```bash
pytest --cov=src --cov-report=term-missing
```

Generate HTML report:

```bash
pytest --cov=src --cov-report=html
```

Coverage report will be generated in:

```text
htmlcov/
```

Open:

```text
htmlcov/index.html
```

in your browser.

---

## Running the Application

A small terminal interface is included to demonstrate functionality.

Run:

```bash
python main.py
```

You will see:

```text
Roman Numeral Converter
1. Integer -> Roman
2. Roman -> Integer
Choose option:
```

### Example: Integer → Roman

```text
Choose option: 1
Enter integer: 1994
Roman numeral: MCMXCIV
```

### Example: Roman → Integer

```text
Choose option: 2
Enter roman numeral: XL
Integer: 40
```

---

## Development Approach

This project was developed following **Test-Driven Development (TDD)** principles:

```text
RED → GREEN → REFACTOR
```

Workflow:

1. Write a failing test
2. Implement the minimum code required
3. Make the test pass
4. Refactor safely
5. Repeat

The implementation evolved incrementally from simple hardcoded cases to a generalized Roman numeral conversion algorithm.

---

## Refactors Performed

### Refactor #1

Replaced multiple conditional statements with a mapping-based greedy algorithm for integer-to-roman conversion.

### Refactor #2

Centralized Roman numeral mappings to simplify reverse conversion and reduce duplication.

---

## Author

Alejandro Sardinas