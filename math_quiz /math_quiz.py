import random

def random_int_in_range(minimum, maximum):
    """
    Returns a random integer between minimum and maximum values, inclusive.
    """
    return random.randint(minimum, maximum)

def random_operator():
    """
    Chooses a random arithmetic operator (+, -, *).
    """
    return random.choice(['+', '-', '*'])

def create_problem(num1, num2, operator):
    """
    Formats a math problem string and calculates the correct answer based on the operator provided.
    """
    problem_statement = f"{num1} {operator} {num2}"
    if operator == '+':
        solution = num1 + num2
    elif operator == '-':
        solution = num1 - num2
    elif operator == '*':
        solution = num1 * num2
    return problem_statement, solution

def run_math_quiz():
    """
    Starts a simple math quiz with multiple-choice questions and scores based on correct answers.
    """
    score = 0
    total_problems = 3

    print("Welcome to the Math Quiz!")
    print("Solve each math problem to the best of your ability.")

    for _ in range(total_problems):
        # Generate random numbers and an operator
        first_num = random_int_in_range(1, 10)
        second_num = random_int_in_range(1, 5)
        operator = random_operator()

        # Create a math problem
        problem, correct_solution = create_problem(first_num, second_num, operator)
        print(f"\nSolve: {problem}")

        # Get user answer and handle invalid input
        try:
            user_solution = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer value.")
            continue  # Move to the next question if input is invalid

        # Validate answer and update score
        if user_solution == correct_solution:
            print("That's correct! +1 point.")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {correct_solution}.")

    print(f"\nQuiz complete! Your final score is: {score}/{total_problems}")

if __name__ == "__main__":
    run_math_quiz()
