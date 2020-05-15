from add import add
import unittest

class TestSum(unittest.TestCase):

    def test_true(self):
        assert add(1, 2) == 3

if __name__=="__main__":
    unittest.main()