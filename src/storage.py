import os
import csv

from typing import Literal

def load_data(data_file: str, sortby: Literal["priority", "deadline"]=None):
    """Loads todo data from a file.

    The file should be in a CSV format with four columns: content, priority,
    deadline and status. The priority column should contain a number, with 0
    corresponding to high, 1 to medium, and 2 to low. The deadline should be
    in the ISO 8601 format, YYYY-MM-DD. The status column should be either
    "todo" or "done".

    Args:
        data_file: The path to the file containing the data.

    Returns:
        A list of dictionaries, each containing a todo item with the keys
        content, priority, deadline and status.

    Raises:
        AssertionError: If the file does not contain the required columns or
            if the priority is not a number or is not one of the allowed values.
    """

    assert os.path.isfile(data_file), "data file does not exist"

    with open(data_file, 'r') as f:
        csv_reader = csv.reader(f)
        
        # skip header
        header = next(csv_reader)
        assert len(header) == 4
        assert header[0] == "content"
        assert header[1] == "priority"
        assert header[2] == "deadline"
        assert header[3] == "status"

        data = [
            {
                "content": row[0], 
                "priority": row[1], 
                "deadline": row[2], 
                "status": row[3]
            } for row in csv_reader]
    
    if sortby == "priority":
        data = sorted(data, key=lambda x: x["priority"], reverse=True)
    elif sortby == "deadline":
        data = sorted(data, key=lambda x: x["deadline"])

    # add number
    data = [
        {
            "index": f"{i + 1:03d}",
            "content": entry["content"],
            "priority": int(entry["priority"]),
            "deadline": entry["deadline"],
            "status": int(entry["status"])
        } for i, entry in enumerate(data)
    ]


    return data


def save_data(data: list, data_file: str):
    """Saves todo data to a file.

    The file should be in a CSV format with four columns: content, priority,
    deadline and status. The priority column should contain a number, with 0
    corresponding to high, 1 to medium, and 2 to low. The deadline should be
    in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, YYYY-MM-DD. The status column should be either
    "todo" or "done".

    Args:
        data: A list of dictionaries, each containing a todo item with the keys
            content, priority, deadline and status.
        data_file: The path to the file to save the data to.

    Raises:
        AssertionError: If the data is not a list of dictionaries.
    """

    assert isinstance(data, list)
    assert all(isinstance(entry, dict) for entry in data)

    with open(data_file, 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(["content", "priority", "deadline", "status"])

        if len(data) == 0:
            return
        
        for entry in data:
            csv_writer.writerow([entry["content"], entry["priority"], entry["deadline"], entry["status"]])
