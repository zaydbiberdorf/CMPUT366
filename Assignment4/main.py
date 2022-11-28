import time
from grid import Grid
from plot_results import PlotResults

def select_variable_fa(grid):
    return None

def select_variable_mrv(grid):
    return None

def search(grid, var_selector):
    return None, False

def forward_checking(grid, variable):
    return None

def pre_process_forward_checking(grid):
    return None

file = open('tutorial_problem.txt', 'r')
problems = file.readlines()
for p in problems:
    g = Grid()
    g.read_file(p)

    # test your backtracking implementation without inference here
    # this test instance is only meant to help you debug your backtracking code
    # once you have implemented forward checking, it is fine to find a solution to this instance with inference

file = open('top95.txt', 'r')
problems = file.readlines()

for p in problems:
    g = Grid()
    g.read_file(p)
    
    # test your backtracking implementation with inference here