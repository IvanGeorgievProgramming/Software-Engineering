# Flake 8 linter

## Installation

```bash
pip install flake8
```

## Example with bad code

```bash
flake8 bad_code.py
```
```
bad_code.py:1:1: F401 'os' imported but unused
bad_code.py:3:1: E302 expected 2 blank lines, found 1
bad_code.py:4:3: E114 indentation is not a multiple of 4 (comment)
bad_code.py:5:3: E111 indentation is not a multiple of 4
bad_code.py:5:9: E703 statement ends with a semicolon
bad_code.py:6:3: E111 indentation is not a multiple of 4
bad_code.py:7:3: E111 indentation is not a multiple of 4
bad_code.py:7:17: E225 missing whitespace around operator
bad_code.py:7:21: E261 at least two spaces before inline comment
bad_code.py:8:3: E111 indentation is not a multiple of 4
bad_code.py:8:18: E231 missing whitespace after ','
bad_code.py:10:1: E302 expected 2 blank lines, found 1
bad_code.py:11:3: E111 indentation is not a multiple of 4
bad_code.py:13:80: E501 line too long (100 > 79 characters)
bad_code.py:15:23: E702 multiple statements on one line (semicolon)
bad_code.py:15:43: E261 at least two spaces before inline comment
bad_code.py:17:3: E111 indentation is not a multiple of 4
bad_code.py:17:22: E261 at least two spaces before inline comment
bad_code.py:20:5: F841 local variable 'unused_var' is assigned to but never used
bad_code.py:22:1: E302 expected 2 blank lines, found 1
bad_code.py:22:24: E261 at least two spaces before inline comment
bad_code.py:23:3: E114 indentation is not a multiple of 4 (comment)
bad_code.py:23:3: E265 block comment should start with '# '
bad_code.py:24:3: E114 indentation is not a multiple of 4 (comment)
bad_code.py:25:3: E111 indentation is not a multiple of 4
bad_code.py:29:1: E265 block comment should start with '# '
bad_code.py:30:1: E305 expected 2 blank lines after class or function definition, found 1
bad_code.py:34:1: E302 expected 2 blank lines, found 0
bad_code.py:42:2: E111 indentation is not a multiple of 4
bad_code.py:42:16: E261 at least two spaces before inline comment
bad_code.py:43:2: E111 indentation is not a multiple of 4
bad_code.py:43:29: E261 at least two spaces before inline comment
bad_code.py:44:2: E111 indentation is not a multiple of 4
bad_code.py:44:22: E261 at least two spaces before inline comment
bad_code.py:45:2: E111 indentation is not a multiple of 4
bad_code.py:46:2: E114 indentation is not a multiple of 4 (comment)
bad_code.py:46:48: W292 no newline at end of file
```

## Example with bad code

```bash
flake8 good_code.py
```
```
There was no result.