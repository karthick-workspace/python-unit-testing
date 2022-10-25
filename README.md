# python-unit-testing

Unit tests automate the repetitive testing process and saves time

# Mocking

Mocking is creating a fake object that represents the "real" object
Allows more control over your code' behavior
Python mock objects provide deeper insight into your code

    * When functions were called
    * How many times they were called
    * What arguments were passed

## Python unit testing libraries

* Pytest
* unitest
* unitest.mock
* nosetests
* doctest

## Environment Setup
**Python 3 is required**

Go to terminal and navigate to your project root folder
```shell
python3 -m venv venv
source ./venv/bin/activate
pip install pytest
pip install unittest2
pip install pyspark 
pip install requests
```

## Running Steps

#### Run all test case in the tests package

```shell
pytest tests
```

#### Run specific test case in the tests package

```shell
pytest tests/unittests/arithmetic_test.py
```
