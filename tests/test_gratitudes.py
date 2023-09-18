from lib.gratitudes import *

def test_gratitudes_adds_gratitude():
    gratitude = Gratitudes()
    gratitude.add("test")
    
def test_gratitude_initial_format_is_correct():
    gratitude = Gratitudes()
    gratitude.add("Be grateful for: ")
    gratitude.format == "Be grateful for: "

def test_returns_list_of_formatted_gratitudes():
    gratitude = Gratitudes()
    gratitude.add("Be grateful for: " + "test") 
    gratitude.format == ["Be grateful for: ", ]
    gratitude.format == "Be grateful for: "


