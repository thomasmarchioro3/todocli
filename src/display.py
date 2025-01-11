from copy import deepcopy

from src.deadline import get_display_deadline
from src.priority import num2priority

STATUS = ["todo", "done"]

def num2status(status: str):
    """
    For the time being, it only maps the status number to a string.
    """
    status = int(status)
    return STATUS[status]

def get_max_display_width(data: dict) -> dict[str, int]:

    max_display_dict = {key: 0 for key in data[0].keys()}

    for entry in data:
        for key in entry.keys():
            if max_display_dict[key] < len(entry[key]):
                max_display_dict[key] = len(entry[key])

    for key in max_display_dict.keys():
        max_display_dict[key] = max(max_display_dict[key], len(key))

    for key in max_display_dict.keys():
        max_display_dict[key] += 2

    return max_display_dict


# def get_max_display_width_v2(data: dict) -> dict[str, int]:

#     max_display_dict = {
#         key: max(len(entry[key]) for entry in data) for key in data[0].keys()
#     }

#     for key in max_display_dict.keys():
#         max_display_dict[key] = max(max_display_dict[key], len(key))

#     for key in max_display_dict.keys():
#         max_display_dict[key] += 2

#     return max_display_dict

def display_data(data: list):

    if len(data) == 0:
        print("\nNo entries in the todo list. Use the 'add' option to add an entry.\n")
        return

    # avoid modifying original data
    data = deepcopy(data)

    # Add weekday to deadline
    for i, todo in enumerate(data):
        data[i]["deadline"] = get_display_deadline(todo["deadline"])
        data[i]["priority"] = num2priority(todo["priority"])
        data[i]["status"] = num2status(todo["status"])

    max_display_dict = get_max_display_width(data)

    formatted_data = ""

    header = "|".join(key.ljust(max_display_dict[key]) for key in max_display_dict.keys())
    separator = "+".join("-" * max_display_dict[key] for key in max_display_dict.keys())

    formatted_data += f"{separator}\n"
    formatted_data += f"{header}\n"
    formatted_data += f"{separator}\n"

    for todo in data:
        entry = "|".join(value.ljust(max_display_dict[key]) for key, value in todo.items())
        formatted_data += f"{entry}\n"
    
    formatted_data += f"{separator}\n"

    print(formatted_data)