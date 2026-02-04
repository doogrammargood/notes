from unittest.mock import patch, call   
from unittest import TestCase
from comprehensions_hw import *
import unittest
from collections import Counter


class CreateTests(TestCase):
    def test_problem_1(self):
        answer = problem_1()
        assert answer == "Lorem Ipsum Dolor Sit Amet, Consectetur Adipiscing Elit, Sed Do Eiusmod Tempor Incididunt Ut Labore Et Dolore Magna Aliqua. Ut Enim Ad Minim Veniam, Quis Nostrud Exercitation Ullamco Laboris Nisi Ut Aliquip Ex Ea Commodo Consequat. Duis Aute Irure Dolor In Reprehenderit In Voluptate Velit Esse Cillum Dolore Eu Fugiat Nulla Pariatur. Excepteur Sint Occaecat Cupidatat Non Proident, Sunt In Culpa Qui Officia Deserunt Mollit Anim Id Est Laborum."
    def test_problem_2(self):
        answer = problem_2()
        assert answer == "Ecpersn cactcpdttnnpodn,sn nclaqiofcadsrn oltai detlbrm"
    def test_problem_3(self):
        initial_string:str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        answer = problem_3()
        assert answer == dict(Counter(initial_string))
if __name__=="__main__":
    unittest.main()