SWEEP_INTERVAL_SECONDS = 30

SWEEP_BATCH = 100


def sweeps_in(seconds: int) -> int:
    if seconds <= 0:
        return 0
    return seconds // SWEEP_INTERVAL_SECONDS


def batches_for(items: int) -> int:
    if items <= 0:
        return 0
    return (items + SWEEP_BATCH - 1) // SWEEP_BATCH
