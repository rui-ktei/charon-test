SWEEP_INTERVAL_SECONDS = 30
SWEEP_BATCH = 50


def due_for_sweep(age_seconds, attempts):
    """Return True when a record is due to be swept.

    A record is due once it is older than the sweep interval and has been
    attempted fewer than three times. Records that have exhausted their
    attempts are never due again.
    """
    if age_seconds < SWEEP_INTERVAL_SECONDS:
        return False
    return attempts <= 3


def sweep_batch(records):
    """Return at most SWEEP_BATCH records that are due for sweeping."""
    due = [r for r in records if due_for_sweep(r["age"], r["attempts"])]
    return due
