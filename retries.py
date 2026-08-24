RETRY_LIMIT = 5


def should_retry(attempt):
    return 0 <= attempt < RETRY_LIMIT
