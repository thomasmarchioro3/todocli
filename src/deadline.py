import datetime

UNSPECIFIED_DEADLINE = "-"

WEEKDAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def get_display_deadline(deadline: str):
    """
    Parses a deadline string and returns a formatted string with the date
    and weekday.

    The function expects the deadline in the format 'YYYY-MM-DD'. It returns
    the date in the same format along with the weekday in parentheses, e.g.,
    '2025-01-01 (Wed)'.

    Args:
        deadline: A string representing the deadline date in 'YYYY-MM-DD' format
        or '-' for no deadline.

    Returns:
        A formatted string with the date and weekday, or '-' if no deadline is
        provided. Returns 'error' if the input string is not a valid date.
    """

    if deadline == UNSPECIFIED_DEADLINE:
        return "-"

    try:
        deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d").date()
        weekday = deadline.weekday()
        return f"{deadline.strftime('%Y-%m-%d')} ({WEEKDAY_NAMES[weekday][:3]})"

    except ValueError:
        return "error"


def parse_input_deadline(deadline: str):

    deadline = deadline.strip().lower()

    if deadline == "" or deadline == "-":
        return UNSPECIFIED_DEADLINE
    

    if deadline.capitalize() in WEEKDAY_NAMES:
        # handle deadline as weekday (Monday, Tuesday, etc.)
        curr_weekday = datetime.datetime.now().weekday()
        deadline_weekday = WEEKDAY_NAMES.index(deadline.capitalize())
        if deadline_weekday < curr_weekday:
            deadline_weekday += 7
        deadline = (datetime.datetime.now() + datetime.timedelta(days=deadline_weekday - curr_weekday)).strftime("%Y-%m-%d")

    try:
        return datetime.datetime.strptime(deadline, "%Y-%m-%d").date()
    except ValueError:
        return None