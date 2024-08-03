# dbsys

dbsys is a Python library for managing database operations using SQLAlchemy and pandas. It provides a high-level interface for common database operations, including reading, writing, creating tables, deleting tables, deleting columns, and deleting rows.

[![PyPI version](https://badge.fury.io/py/dbsys.svg)](https://badge.fury.io/py/dbsys)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Installation

You can install the latest version of dbsys using pip:

```
pip install --upgrade dbsys
```

For a specific version:

```
pip install dbsys==0.1.4
```

## Installation

You can install dbsys using pip:

```
pip install dbsys
```

## Features

- Read entire tables
- Write data to tables
- Create new tables
- Delete tables
- Delete specific columns
- Delete specific rows

## Usage

Here's a quick example of how to use dbsys:

```python
from dbsys import manage_db
import pandas as pd

# Create a sample DataFrame
data = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})

# Database URL
db_url = "sqlite:///example.db"

# Create a new table
manage_db(db_url, "my_table", "c", data)

# Read the table
result = manage_db(db_url, "my_table", "r")
print(result)

# Delete a column
manage_db(db_url, "my_table", "dc", column_name="B")

# Delete a row
manage_db(db_url, "my_table", "dr", row_identifier={"A": 2})

# Delete the table
manage_db(db_url, "my_table", "dt")
```

## API Reference

### `manage_db(database_url: str, table_name: str, operation: str, data: Optional[pd.DataFrame] = None, column_name: Optional[str] = None, row_identifier: Optional[Dict[str, Any]] = None) -> Optional[pd.DataFrame]`

Manage database tables using pandas dataframes and SQLAlchemy.

Parameters:
- `database_url` (str): URL of the database to connect to.
- `table_name` (str): Name of the table to operate on.
- `operation` (str): Operation to perform. Valid options are:
  - 'r' or 'read': Read the entire table.
  - 'w' or 'write': Write data to the table, replacing existing data.
  - 'c' or 'create': Create a new table with the provided data.
  - 'dt' or 'delete table': Delete the entire table.
  - 'dc' or 'delete column': Delete a specific column from the table.
  - 'dr' or 'delete row': Delete a specific row from the table.
- `data` (Optional[pd.DataFrame]): DataFrame to write or create table with. Required for 'w' and 'c' operations.
- `column_name` (Optional[str]): Name of the column to delete. Required for 'dc' operation.
- `row_identifier` (Optional[Dict[str, Any]]): Dictionary containing column:value pair to identify the row to delete. Required for 'dr' operation.

Returns:
- Optional[pd.DataFrame]: DataFrame representing the current state of the table after the operation, or None for delete operations.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

If you encounter any problems or have any questions, please [open an issue](https://github.com/lifsys/dbsys/issues) on our GitHub repository.
## About Lifsys, Inc

Lifsys, Inc is an AI company dedicated to developing solutions for the future. For more information, visit [www.lifsys.com](https://www.lifsys.com).
