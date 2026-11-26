"""Replace TODOs with your own code. Run to check your work."""
import csv
from pathlib import Path

with (Path(__file__).parent / "data" / "practice_transactions.csv").open(newline="", encoding="utf-8") as file:
    rows = list(csv.DictReader(file))

def total_volume(records):
    # TODO: return sum of integer amount_usd values.
    pass

def screen_ids(records, threshold):
    # TODO: return list of IDs whose amount >= threshold.
    pass

def outgoing_total(records, account):
    # TODO: sum amounts where source_account equals account.
    pass

def incoming_total(records, account):
    # TODO: sum amounts where destination_account equals account.
    pass

if __name__ == "__main__":
    assert total_volume(rows) == 14000
    assert screen_ids(rows, 5000) == ["P003", "P005"]
    assert outgoing_total(rows, "P001") == 6200
    assert incoming_total(rows, "P001") == 7500
    assert screen_ids(rows, 20000) == []
    print("All practice checks passed.")
