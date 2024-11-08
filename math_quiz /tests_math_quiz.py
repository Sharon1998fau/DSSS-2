import unittest
from math_quiz import random_int_in_range, random_operator, create_problem

class MathQuizTestCases(unittest.TestCase):
    """
    Test suite for the math quiz functions.
    """

    def test_random_integer_within_range(self):
        # Test if generated integers fall within the specified range
        result = random_int_in_range(1, 10)
        self.assertGreaterEqual(result, 1, "Result should be greater than or equal to 1")
        self.assertLessEqual(result, 10, "Result should be less than or equal to 10")

        result = random_int_in_range(5, 15)
        self.assertGreaterEqual(result, 5, "Result should be greater than or equal to 5")
        self.assertLessEqual(result, 15, "Result should be less than or equal to 15")

    def test_random_operator_selection(self):
        # Check if the returned operator is one of the expected values
        operator = random_operator()
        self.assertIn(operator, ['+', '-', '*'], "Operator should be one of '+', '-', '*'")

    def test_create_problem_output(self):
        # Test the output format and correctness of the answer for each operator
        problem_str, solution = create_problem(5, 3, '+')
        self.assertEqual(problem_str, "5 + 3", "Problem string should match '5 + 3'")
        self.assertEqual(solution, 8, "Solution should be 8")

        problem_str, solution = create_problem(5, 3, '-')
        self.assertEqual(problem_str, "5 - 3", "Problem string should match '5 - 3'")
        self.assertEqual(solution, 2, "Solution should be 2")

        problem_str, solution = create_problem(5, 3, '*')
        self.assertEqual(problem_str, "5 * 3", "Problem string should match '5 * 3'")
        self.assertEqual(solution, 15, "Solution should be 15")

if __name__ == '__main__':
    unittest.main()
