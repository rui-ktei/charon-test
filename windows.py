WINDOW_SECONDS = 30


def window_for(attempt):
    if attempt < 1:
        return WINDOW_SECONDS
    else:
        return WINDOW_SECONDS * attempt
