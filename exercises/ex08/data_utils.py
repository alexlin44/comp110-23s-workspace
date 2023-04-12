"""Data wrangling activity."""

__author__ = "730465832"

from csv import DictReader

DATA_DIRECTORY= "../../data"
DATA_FILE_PATH= f"{DATA_DIRECTORY}/nc_durham_2015_march_21_to_26.csv"


def read_csv_rows(DATA_FILE_PATH: str) -> list[dict[str, str]]:
    """Reads an entire csv into a list of rows, each row is a dictionary with column headers as keys and row values as values."""
    rows: list[dict[str, str]] = []
    file_handle = open(DATA_FILE_PATH, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        rows.append(row)
    file_handle.close()
    return rows


def column_values(rows: list[dict[str, str]], column: str) -> list[str]:
    """Produces a list of all values in a single column."""
    values: list[str] = []
    for row in rows:
        if column in row:
            values.append(row[column])
    return values


def columnar(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms a list of rows into a dictionary of columns."""
    columns: dict[str, list[str]] = {}
    for row in rows:
        for column, value in row.items():
            if column not in columns:
                columns[column] = []
            columns[column].append(value)
    return columns


def head(data: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Returns a new column-based table with only the first n rows of data for each column."""
    result = {}
    for column_name, column_values in data.items():
        result[column_name] = column_values[:n]
    return result


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produces a new table with only the specified columns."""
    result: dict[str, list[str]] = {}
    for column in columns:
        result[column] = table[column]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    result = {}

    # loop through each column in table1
    for column in table1:
        result[column] = table1[column]

    # loop through each column in table2
    for column in table2:
        if column in result:
            result[column].extend(table2[column])
        else:
            result[column] = table2[column]

    return result


def count(list1: list[str]) -> dict[str, int]:
    """Counts the frequency of each item in a list."""
    result: dict[str, int] = {}
    for item in list1:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result