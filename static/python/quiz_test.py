import unittest
from quiz import *

assert question_one_answer("b") == "answer ok and correct"
assert question_one_answer("B") == "answer ok and correct"
assert question_one_answer("c") == "answer ok but incorrect"

print("All tests passed")