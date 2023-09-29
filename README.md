# CS-555-Agile

## Folder structure:

- main.py : the top most file, where the code should start.
- printOutput.py: This will print output of the code on the console as well as in text file.
- filters.py: Data filtering based on different aspects should be merged here.
- Initialparser.py: Tagging of each of the input based on "valid" tag. ("valid" tags are the once which will be used for the ouputing all the relevant data in
  the console or in the text file).

## Installation and Execution:

Step-1: **Create a virtual environment** <br>

### For Linux/Mac: <br>

`virtualenv -p /usr/bin/python3 vir_env` <br>

`source vir_env/bin/activate` <br>

check whether the virtual enviornment is properly setup and is running: <br>

`pip -V` or `pip --version`

It should display directory where you have setup your virtual enviornment.

### For Windows: <br>

`python -m venv vir_env` <br>

`vir_env\Scripts\activate` <br>

`pip -V` or `pip --version`

It should display directory where you have setup your virtual enviornment.

Step-2: **Installing dependencies** <br>

execute the command: `pip install -r requirements.txt`

Step-3: **Running the code** <br>

For Linux/Mac:<br>
in the console execute the command `python3 main.py` <br>

For windows: <br>
in the console execute the command `python main.py` <br>
