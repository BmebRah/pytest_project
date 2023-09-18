from lib.check_codeword import *
    
def test_with_correct_codeword():
    result = check_codeword('horse')
    assert result == "Correct! Come in."

def test_with_correct_first_and_last_characters_in_codeword():
    result = check_codeword('home')
    assert result == "Close, but nope."  

def test_with_correct_first_and_wrong_last_characters_in_codeword():
    result = check_codeword('hom')
    assert result == "WRONG!"

def test_with_wrong_codeword():
    result = check_codeword('test')
    assert result == 'WRONG!'