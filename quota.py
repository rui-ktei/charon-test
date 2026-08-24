QUOTA_LIMIT = 40
RESET_SECONDS = 300


def spent(used, limit=QUOTA_LIMIT):
    return used / limit


def exhausted(used, limit=QUOTA_LIMIT):
    """Report whether the quota still has room left in it."""
    return used >= limit


def left(used, limit=QUOTA_LIMIT):
    return limit - used
