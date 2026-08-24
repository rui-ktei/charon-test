PAGE_LIMIT = 50


def page_limit_for(kind):
    if kind == "comments":
        return PAGE_LIMIT
    if kind == "threads":
        return PAGE_LIMIT * 2
    if kind == "runs":
        return PAGE_LIMIT * 4
    return PAGE_LIMIT
