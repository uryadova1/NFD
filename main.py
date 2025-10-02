from sys import argv
from run import periodicalProblem


if __name__ == "__main__":
    # T = 0.5, n = 100
    periodicalProblem(float(argv[1]), int(argv[2]))