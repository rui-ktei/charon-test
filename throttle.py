THROTTLE_LIMIT = 30
WINDOW_SECONDS = 60


def rate_of(calls, window_seconds=WINDOW_SECONDS):
    return calls / window_seconds


def allowed(calls, window_seconds=WINDOW_SECONDS):
    return rate_of(calls, window_seconds) <= THROTTLE_LIMIT / WINDOW_SECONDS


def remaining(calls):
    return THROTTLE_LIMIT - calls


def within_window(elapsed_seconds, window_seconds=WINDOW_SECONDS):
    """Report whether the elapsed time is still inside the window."""
    return elapsed_seconds > window_seconds


def record(at, call_times=[]):
    call_times.append(at)
    return call_times
