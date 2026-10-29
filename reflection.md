# Lab 5 — Reflection

## 1. What is static code analysis, and why is it useful?

Static code analysis checks source code without executing the program. It helps find possible bugs, security risks, and style problems early. This improves code quality and maintainability.

## 2. What are the differences between Pylint, Bandit, and Flake8?

Pylint checks code quality and common programming mistakes. Bandit identifies potential security problems. Flake8 checks Python style and formatting. Using all three provides broader coverage of code issues.

## 3. What issues did you find and fix?

The original program contained unsafe `eval()` usage, weak MD5 hashing, insecure random PIN generation, a hard-coded token, shell command execution, a mutable default argument, and broad exception handling. I replaced unsafe operations, improved validation and file handling, and corrected naming and formatting issues.

## 4. What did you learn from this lab?

I learned that a program can run successfully while still containing security and quality problems. Static analysis tools help identify these issues, but the results must be reviewed and the program must be tested after changes. The final Pylint score improved from 5.62/10 to 9.81/10, Bandit reported no issues, and Flake8 reported no remaining style issues.