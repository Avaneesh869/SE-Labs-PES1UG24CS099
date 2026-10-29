"""Bank account management module with safer input handling and backups."""

import hashlib
import json
import secrets
from pathlib import Path

account_data = {}


def create_account(acc_id, name, initial_deposit=0.0):
    """Create an account with an initial balance."""
    if acc_id in account_data or initial_deposit < 0:
        return False

    account_data[acc_id] = {
        "name": name,
        "balance": float(initial_deposit),
        "transactions": [
            f"Created {acc_id} with initial balance {initial_deposit:.2f}"
        ],
    }
    return True


def deposit(acc_id, amount):
    """Deposit a positive amount and report success or failure."""
    account = account_data.get(acc_id)
    if account is None or amount <= 0:
        return False

    account["balance"] += amount
    account["transactions"].append(f"Deposited {amount:.2f}")
    return True


def withdraw(acc_id, amount):
    """Withdraw money when the account has sufficient funds."""
    account = account_data.get(acc_id)
    if account is None or amount <= 0:
        return False

    if account["balance"] < amount:
        return False

    account["balance"] -= amount
    account["transactions"].append(f"Withdrew {amount:.2f}")
    return True


def compute_bonus(acc_id, rate=0.05):
    """Calculate a bonus using a validated rate instead of eval."""
    account = account_data.get(acc_id)
    if account is None:
        raise ValueError(f"Unknown account: {acc_id}")

    if not 0 <= rate <= 1:
        raise ValueError("Bonus rate must be between 0 and 1.")

    return account["balance"] * rate


def get_hash(pin):
    """Return a SHA-256 digest for demonstration purposes."""
    return hashlib.sha256(pin.encode("utf-8")).hexdigest()


def generate_temp_pin():
    """Generate a four-digit temporary PIN securely."""
    return secrets.randbelow(9000) + 1000


def backup_data(filename="backup.json"):
    """Save account data as JSON and return the backup path."""
    backup_path = Path(filename)

    with backup_path.open("w", encoding="utf-8") as backup_file:
        json.dump(account_data, backup_file, indent=2)

    return backup_path


def main():
    """Run a demonstration of the bank account system."""
    create_account("A01", "Alice", 1000)
    deposit("A01", 500)
    withdraw("A01", 200)

    print(f"Bonus: {compute_bonus('A01'):.2f}")
    print(f"PIN Hash: {get_hash('1234')}")
    print(f"Temp PIN: {generate_temp_pin()}")

    backup_path = backup_data()
    print(f"Backup written to: {backup_path}")


if __name__ == "__main__":
    main()
