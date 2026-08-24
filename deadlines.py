DEADLINE_SECONDS = 60


def deadline_for(kind):
    if kind == "poll":
        return DEADLINE_SECONDS
    if kind == "merge":
        return DEADLINE_SECONDS * 2
    if kind == "release":
        return DEADLINE_SECONDS * 5
    return DEADLINE_SECONDS
