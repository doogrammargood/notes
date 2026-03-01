from unittest.mock import patch, call   
from unittest import TestCase
from example_starter_code_for_maze import *
import unittest

class CreateTests(TestCase):
    @patch("builtins.print") 
    def test_exit_exists(self,mocked_print):
        maze = generate_maze(WIDTH, HEIGHT)
        print(call("E") in mocked_print.mock_calls)

if __name__=="__main__":
    unittest.main()
