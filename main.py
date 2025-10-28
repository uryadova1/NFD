from sys import argv

from const import art_vis_coeffs_count
from run import periodicalProblem
from tasks import task13, task_relative_errors_and_local_orders_1

if __name__ == "__main__":
    # T = 0.5, n = 100
    # periodicalProblem(float(argv[1]), int(argv[2]))
    # task13()
    task_relative_errors_and_local_orders_1()
