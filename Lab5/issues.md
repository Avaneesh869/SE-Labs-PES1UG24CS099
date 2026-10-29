# Lab 5 — Static Code Analysis Issues

The line numbers below refer to the original `bank_account_system.py`.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe `eval()` | Security — Medium | 39 | `eval()` can execute arbitrary Python expressions, creating a security risk. | Replaced expression evaluation with a bonus calculation using a validated rate. |
| Weak MD5 hash | Security — High | 44 | MD5 is not suitable for protecting authentication secrets. | Changed the demonstration digest to SHA-256. Production PIN storage requires a dedicated password-hashing method. |
| Shell command injection risk | Security — High | 55 | `os.system()` executes a shell command using a filename that could contain malicious input. | Removed the shell command and used safer file handling. |
| Insecure random PIN generation | Security — Low | 48 | `random.randint()` is not designed for security-sensitive random values. | Replaced it with `secrets.randbelow()`. |
| Hard-coded admin token | Security — Low | 59 | A secret token is stored directly in the source code and printed. | Removed the hard-coded token and its print statement. |
| Mutable default argument | Bug — Medium | 11 | `transactions=[]` can be shared between function calls. | Created a separate transaction list for each account. |
| Bare exception handling | Reliability — Medium | 22 | `except: pass` hides errors and makes failed deposits difficult to detect. | Added account and amount validation and returned a success/failure result. |
| Unsafe backup handling | Reliability — Medium | 51–56 | Manual file handling and shell execution make backups less reliable and potentially unsafe. | Used a context manager and JSON serialization. |
| Unused import and variable | Maintainability — Low | 6, 27 | `sys` and `service_fee` were unused. | Removed unused code. |
| Naming and documentation issues | Style — Low | 11, multiple | The original function name did not follow snake_case, and several functions lacked docstrings. | Renamed the function and added docstrings. |

## Summary

Static analysis identified security, reliability, maintainability, and style problems. The program was updated, and Pylint, Bandit, and Flake8 were rerun to verify the improvements.