import unittest
from quiz2 import *

"""Assertions that question answers are being read correctly"""
assert answer_given.lower() == a_str.lower(), "Correct"
assert answer_given.lower() == "", "No answer given"
assert answer_given.lower() != a_str.lower(), "Wrong!"

print("All tests passed")