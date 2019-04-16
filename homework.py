# Homework
#
# """
# This is a list of functions that should be completed.
# """

from typing import Any
from typing import List


class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(first: Any, second: Any) -> bool:
    return first == second
    pass


def is_two_objects_has_same_type(first: Any, second: Any) -> bool:
    return type(first) == type(second)
    pass


def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:
    return id(first) == id(second)
    pass


def multiple_ints(first_value: int, second_value: int) -> int:
    return first_value * second_value
    pass


def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    return int(first_value) * int(second_value)
    pass


def is_word_in_text(word: str, text: str) -> bool:
    if word in text:
        return True
    else:
        return False
    pass


def some_loop_exercise() -> list:
    return list(range(0, 13))[:6] + list(range(0, 13))[8:]
    pass


def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    index = len(data) - 1
    while index >= 0:
        if data[index] < 0:
            del data[index]
        index = index - 1
    return data
    pass


def alphabet() -> dict:
    dict = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8',
    'i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17',
    'r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'}
    return dict
    pass


def simple_sort(data: List[int]) -> List[list]:
    for index in range(len(data) - 1, 0, -1):
        for i in range(index):
            if data[i] > data[i + 1]:
                temp = data[i]
                data[i] = data[i + 1]
                data[i + 1] = temp
    return data
    pass