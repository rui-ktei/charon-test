SHUTDOWN_HOUR = 19
STARTUP_HOUR = 7


def within_window(hour: int) -> bool:
    if STARTUP_HOUR <= SHUTDOWN_HOUR:
        return STARTUP_HOUR <= hour < SHUTDOWN_HOUR
    return hour >= STARTUP_HOUR or hour < SHUTDOWN_HOUR
