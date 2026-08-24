WINDOW_SECONDS = 30


def window_for(attempt):
    return WINDOW_SECONDS * max(attempt, 1)
