# PyFABDB
[![Test](https://github.com/GonzalezAndrew/pyfabdb/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/GonzalezAndrew/pyfabdb/actions/workflows/test.yml)
[![pre-commit](https://github.com/GonzalezAndrew/pyfabdb/actions/workflows/pre-commit.yml/badge.svg?branch=master)](https://github.com/GonzalezAndrew/pyfabdb/actions/workflows/pre-commit.yml)

PyFABDB is a Python library to access the [Flesh and Blood DB API](https://fabdb.net/resources/api). The Python library enables you to access all public Flesh and Blood DB API endpoints using Python.

## Install
```
$ pip install pyfabdb
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
All help is welcomed!

### 1. Setting up an environment
The easiest way to set up a test environment is to run:

1. `tox --devenv venv`
2. `source venv/bin/activate`

### 2. Running all the tests
After making your changes and creating new test for any changes, you will need to ensure all test pass. Running all the test can be done by running `tox -e py`.

### 3. Install pre-commit
With the environment created by tox, run:

1. `pip install pre-commit`
2. `pre-commit install`

### 4. Create a pull requests
Create a pull request following the pull request template. A maintainer will review the changes made, update the changelog and release the new version of pyfabdb.
