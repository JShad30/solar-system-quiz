import unittest
from quiz import *


"""Assertions for the score count"""
assert question_answer("correct") == 1, "Score now 1 as expected"
assert question_answer("Correct") == 1, "Score now 1 as expected"
assert question_answer("incorrect") == 0, "Score 0 as expected"
assert question_answer("") == 0, "Invalid answer"

print("All tests passed")