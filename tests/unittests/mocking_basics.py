import unittest
from unittest.mock import Mock
from datetime import datetime
import requests
import json
import pytest

tuesday = datetime(year=2022, month=10, day=25)
sunday = datetime(year=2022, month=10, day=23)


def test_mock():
    json = Mock()

    json.dumps({'a': 1})

    json.dumps.assert_called()
    json.dumps.assert_called_once()
    json.dumps.assert_called_with({'a': 1})

    print(json.dumps.call_args)
    print(json.dumps.call_count)


datetime = Mock()


def is_weekday():
    today = datetime.today()
    day_of_the_week = today.weekday()
    return (0 <= day_of_the_week < 5)


def test_weekday():
    datetime.today.return_value = tuesday
    assert is_weekday()


def test_weekday():
    datetime.today.return_value = tuesday
    assert is_weekday()


def test_not_weekday():
    datetime.today.return_value = sunday
    assert not is_weekday()


requests = Mock()


def get_holidays():
    response = requests.get("http://localhost/api/holidays")
    print(requests)
    print(response)

    if response.status_code == 200:
        return response.json()
    return None


class TestGetHolidays(unittest.TestCase):
    def test_get_holidays_connection(self):
        requests.get.side_effect = ConnectionError
        with self.assertRaises(ConnectionError):
            get_holidays()

    def test_get_holidays_response(self):
        # response_mock = self.log_request()
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            "25/12": 'Christmas',
            "01/01": "New Years"
        }

        print(requests)
        print(response_mock)
        print("-------------")

        requests.get.return_value = response_mock

        assert get_holidays()


if __name__ == '__main__':
    unittest.main
