
from src.display import display_data
from src.priority import parse_input_priority, PRIORITY_RANGE
from src.deadline import parse_input_deadline


def add_entry(data: list):

    # display_data(data)

    content = input("Content: ")

    priority = -1
    while priority not in PRIORITY_RANGE:
        priority = input("Priority (high = H, medium = M, low = L) [blank for medium]: ")
        priority = parse_input_priority(priority)
        if priority == -1:
            print("Invalid priority. Please use H, M, or L.")
    deadline = None

    while deadline is None:
        deadline = input("Deadline [YYYY-MM-DD or weekday, blank for no deadline]: ")

        deadline = parse_input_deadline(deadline)

        if deadline is None:
            print("Invalid deadline format. Please use YYYY-MM-DD or a weekday (e.g., monday).")

    data.append({"content": content, "priority": priority, "deadline": deadline, "status": 0})

    return data    


def edit_entry(data: list, index: str):

    if len(data) == 0:
        print("\nNo entries in the todo list. Use the 'add' option to add an entry.\n")
        return data

    index = parse_entry_index(index)

    print("Current entry:")
    display_data([data[index]])

    curr_content = data[index]["content"]
    curr_priority = data[index]["priority"]
    curr_deadline = data[index]["deadline"]

    content = input("Content [blank for current]: ")
    if content == "":
        content = curr_content

    priority = -1
    while priority not in PRIORITY_RANGE:
        priority = input("Priority (high = H, medium = M, low = L) [blank for current]: ")

        if priority.strip() == "":
            priority = curr_priority
        else:
            priority = parse_input_priority(priority)

        if priority == -1:
            print("Invalid priority. Please use H, M, or L.")

    deadline = None
    while deadline is None:
        deadline = input("Deadline [YYYY-MM-DD or weekday, blank for current]: ")

        if deadline.strip() == "":
            deadline = curr_deadline
        else:
            deadline = parse_input_deadline(deadline)

        if deadline is None:
            print("Invalid deadline format. Please use YYYY-MM-DD or a weekday (e.g., monday).")

    data[index]["content"] = content
    data[index]["priority"] = priority
    data[index]["deadline"] = deadline

    return data


def parse_entry_index(index: str):
    """
    Parse the index of the entry to edit or remove. Removes spaces and leading zeros before converting to an integer.

    Args:
        index: The index of the entry to remove.

    Returns:
        The index of the entry to remove.
    """

    index = index.strip()
    index = index.lstrip("0")
    try:
        index = int(index) - 1
        return index
    except ValueError:
        return -1


def remove_entry(data: list, index: str):

    if len(data) == 0:
        print("\nNo entries in the todo list. Use the 'add' option to add an entry.\n")
        return data

    if index is not None:
        index = parse_entry_index(index)
        if index not in range(len(data)):
            # Case when index is out of range
            print("Index should be between 1 and " + str(len(data)) + ".")
            print("")

            display_data(data)
            index = -1
    else:
        # If index is not provided, show the todo list and ask for input
        display_data(data)
        index = -1


    while index not in range(len(data)):
        index = input("Enter index to remove: ")
        index = parse_entry_index(index)

        if index not in range(len(data)):
            print("Index should be between 1 and " + str(len(data)) + ".")

    data.pop(index)

    display_data(data)

    return data