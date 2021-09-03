# PyFABDB

PyFABDB is a Python library to access the [Flesh and Blood DB API](https://fabdb.net/resources/api). The Python library enables you to access all public Flesh and Blood DB API endpoints in Python.

## Install
```
$ pip install <name>
```

## Examples

```python
>>> from pyfabdb import pyfabdb
>>> fabdb = pyfabdb.PyFabdb()
>>> card = fabdb.get_card(id="absorb-in-aether-red")
>>> print(card["name"])
Absorb in Aether
```

## Contributing
