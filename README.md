# JediSQL

這是超好用 API 把 `MySQLdb` 包起來

## Get Start

還沒有打算上傳到 PYPI 請大家直接 `import JediSQL`

### Prerequisite: Install MySQLdb

For Ubuntu

```
sudo apt-get install python-pip python-dev libmysqlclient-dev
pip install MySQL-python
```

## Example

```python
jedi = JediSQL.JediMaster()
```

### None create_database(str)

```python
jedi.create_database("example")
```

### None create_table(str, str, [(str, str)...])

```python
columns = [
  ("date", "DATE"),
  ("time", "TIME"),
  ("supply", "FLOAT")
]
jedi.create_table("your_db", "your_table", columns)
```

### None insert_column(str, str, tuple)

照順序 insert

```python
columns = ("2017-10-10", "05:34:33", 12.3)
jedi.insert_table("your_db", "your_table", columns)
```

### None insert_column_custom(str, str, dict)

順序自己定 insert

```python
columns = {
  "date": "2017-10-10",
  "supply": 10.2
}
jedi.insert_column_custom("your_db", table, columns)
```
