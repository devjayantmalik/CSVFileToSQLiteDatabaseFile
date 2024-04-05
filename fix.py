def read_file():
    with open(".venv/lib/python3.10/site-packages/pandas/io/sql.py", "r") as sqlfile:
        return sqlfile.read()


def fix_pandas():
    content = read_file()
    with open(".venv/lib/python3.10/site-packages/pandas/io/sql.py", "w") as sqlfile:
        try:
            # We already have updated version
            content.index("INSERT OR IGNORE INTO")
            sqlfile.write(content)
        except ValueError:
            # Update pandas sql generation statement
            content = content.replace("INSERT INTO", "INSERT OR IGNORE INTO")
            sqlfile.write(content)


if __name__ == '__main__':
    fix_pandas()
