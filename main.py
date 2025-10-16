from sys import argv
from run import periodicalProblem
from tasks import task13, task_relative_errors_and_local_orders

if __name__ == "__main__":
    # T = 0.5, n = 100
    # periodicalProblem(float(argv[1]), int(argv[2]))
    task13()
    task_relative_errors_and_local_orders()