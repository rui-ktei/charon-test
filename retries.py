RETRY_LIMIT = 5


def should_retry(attempt):
    if attempt < RETRY_LIMIT:
        return True
    else:
        return False
