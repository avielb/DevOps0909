import requests
from os import getenv

def test_get(url_to_test):
    response = requests.get(f"http://{url_to_test}/whatismyname")
    actual = response.text
    expected = "mazda, citroen, chevrolet"
    assert expected == actual


def test_post(url_to_test):
    response = requests.post(f"http://{url_to_test}/whatismyname")
    actual = response.text
    expected = "saved new car"
    assert expected == actual

def test_get_cars(url_to_test):
    response = requests.get(f"http://{url_to_test}/cars")
    my_file = open("cars.txt")
    expected = str(my_file.readlines())
    actual = response.text
    assert expected == actual

# test_get("localhost:5001")
# test_post("localhost:5001")
# test_get_cars(getenv("BASE_URL", "localhost:5001"))