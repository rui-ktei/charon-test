RETRY_LIMIT = 5


def should_retry(attempt):
    return attempt < RETRY_LIMIT
