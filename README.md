# Minimal TO-DO CLI in Python

Minimal TO-DO list CLI written in Python (using only the standard library).

## Installation

Linux:
- Install Python >= [3.10](https://www.python.org/downloads/release/python-3100/)
- Clone the repository
- Navigate to the root directory of the repository and run
```
./setup.sh
```
NOTE: You may need to run `chmod +x setup.sh` first

## Example TO-DO list displayed by CLI

After installation, run `todocli`

```
index  |content    |priority  |deadline             |status  
-------+-----------+----------+---------------------+--------
001    |Get a job  |low       |-                    |todo    
002    |Learn C    |high      |2025-01-13 (Monday)  |todo    
003    |Laundry    |medium    |2025-01-13 (Monday)  |todo    
-------+-----------+----------+---------------------+--------
```

## Usage

- Show entries:
```bash
todocli
```

- Show sorted entries (by "priority" or "deadline"):
```bash
todocli --sortby <COLUMN>
```

- Add a new entry:

```bash
todocli add
```

This will allow to enter a new TO-DO item by specifying content, priority and deadline (the last two can be left blank).
The deadline can be specified either using the format YYYY-mm-dd or by specifying the day of the week (e.g., if "tuesday" is entered, the program will set the deadline to the upcoming Tuesday).


- Remove an entry:

```bash
todocli remove <ENTRY INDEX>
```


## Planned features

TODO
- Add "today" and "tomorrow" to the recognized deadlines
- Add support for other date formats (e.g. "Jan 15")
- Add the possibility to switch between multiple lists