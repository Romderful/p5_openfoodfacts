# OpenFoodFacts - Openclassrooms project 5

The idea of Pur Beurre is to create a program that interacts with the OpenFoodFacts database. This program makes it possible to recover food from the database of OpenFoodFacts, compare them and offer the user a healthier substitute to the food that he chose previously. : [link to github](https://github.com/Romderful/Project3_MacGyver)

## Installation

Clone [the repository](https://github.com/Romderful/Project3_MacGyver) on your computer.

> Set your virtual environment under [python 3.9](https://www.python.org/downloads/release/python-380/)
> Install mysql_server on your computer [mysql_server](https://dev.mysql.com/downloads/mysql/)

```bash
python -m venv .venv  # create the virtual environment
. .venv/Scripts/activate  # activate the virtual environment
pip install -r requirements.txt  # install the dependencies

touch .env # create a file where you'll put your mysql server informations

USER = "your_username"
PASSWORD = "your_password"
HOST = "localhost"
DATABASE = "openfoodfacts"
CHARSET = "utf8"

python install.py # install the dabatase on your computer
```

## Usage

```bash
python main.py
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
