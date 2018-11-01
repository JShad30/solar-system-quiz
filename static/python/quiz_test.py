import unittest
from quiz import *

assert question_one_answer() == "b", "answer ok and correct"
assert question_one_answer() == "c", "answer ok but incorrect"
assert question_one_answer() == "f", "answer invalid"

print("All tests passed")