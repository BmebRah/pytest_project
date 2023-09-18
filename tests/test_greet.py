from lib.greet import *

def test_greet_returns_hello_for_any_name():
    result = greet('name')
    assert result == "Hello, name!"