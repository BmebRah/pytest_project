from lib.counter import *

def test_counter():
    count = Counter()
    count.add(2)
    result = count.report()
    assert result == f"Counted to 2 so far."
def test_counter_in_reverse():
    count = Counter()
    count.add(-1)
    result = count.report()
    assert result  == f"Counted to -1 so far."  