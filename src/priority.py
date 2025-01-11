PRIORITY_LEVELS = ["low", "medium", "high"]

def num2priority(priority: str):

    assert priority.isnumeric()
    priority = int(priority)

    assert priority in range(len(PRIORITY_LEVELS))

    return PRIORITY_LEVELS[priority]


def parse_input_priority(priority: str):

    priority = priority.strip().lower()

    if priority == "":
        return 1

    if priority in ("high", "h"):
        return 2
    elif priority in ("medium", "m"):
        return 1
    elif priority in ("low", "l"):
        return 0
    
    return -1