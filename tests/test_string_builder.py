from lib.string_builder import *

def test_string_builder_returns_empty_string_initially():
    string = StringBuilder()
    string.output == ""
    
def test_string_builder_adds_a_string():
    string = StringBuilder()
    string.add('test')
    assert string.output() == 'test'

def test_string_builder_returns_length_of_string():
    string = StringBuilder()
    string.add('test')
    assert string.size() == 4