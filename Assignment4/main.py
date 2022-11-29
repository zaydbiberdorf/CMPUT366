import time
from grid import Grid
from plot_results import PlotResults
from math import inf
import time

def ac3(grid, var):
    """
        This is a domain-specific implementation of AC3 for Sudoku. 

        It keeps a set of arcs to be processed (arcs) which is provided as input to the method. 
        Since this is a domain-specific implementation, we don't need to maintain a graph and a set 
        of arcs in memory. We can store in arcs the cells of the grid and, when processing a cell, 
        we ensure arc consistency of all variables related to this cell by removing the value of
        cell from all variables in its column, row, and unit. 

        For example, if the method is used as a preprocessing step, then arcs is initialized with 
        all cells that start with a number on the grid. This method ensures arc consistency by
        removing from the domain of all variables in the row, column and unit the values of 
        the cells given as input. The method adds to the set of arcs all variables that have
        their values assigned during the propagation of the contrains. 
    """
    if not type(var) == list:
        arcs = [var]
    else:
        arcs = var
    checked = set()
    while len(arcs):
        cell = arcs.pop()
        checked.add(cell)

        assigned_row, failure = grid.remove_domain_row(cell[0], cell[1])
        if failure: return failure

        assigned_column, failure = grid.remove_domain_column(cell[0], cell[1])
        if failure: return failure

        assigned_unit, failure = grid.remove_domain_unit(cell[0], cell[1])
        if failure: return failure

        arcs.extend(assigned_row)
        arcs.extend(assigned_column)
        arcs.extend(assigned_unit)    
    return False

def pre_process_ac3(grid):
    """
    This method enforces arc consistency for the initial grid of the puzzle.

    The method runs AC3 for the arcs involving the variables whose values are 
    already assigned in the initial grid. 
    """
    arcs_to_make_consistent = []

    for i in range(grid.get_width()):
        for j in range(grid.get_width()):
            if len(grid.get_cells()[i][j]) == 1:
                arcs_to_make_consistent.append((i, j))

    ac3(grid, arcs_to_make_consistent)


def select_variable_fa(grid):
    cells = grid.get_cells()
    for i in range(grid.get_width()):
        for j in range(grid.get_width()):
            if len(cells[i][j]) > 1:
                return (i, j)
                


def select_variable_mrv(grid):
    minLen = inf
    cells = grid.get_cells()
    for i in range(grid.get_width()):
        for j in range(grid.get_width()):
            if len(cells[i][j]) < minLen and len(cells[i][j]) > 1:
                minLen = len(cells[i][j])
                retVal = (i, j)

    return retVal



def search(grid, var_selector):

    '''
    This function will return a grid with the solved state if the grid is solvalbel
    '''

    # base case
    if grid.is_solved():
        return grid, True
    
    # getting the location of the next empty space
    var = var_selector(grid)

    # for each element in the domain check to see if it is a valid choice and keep seaching
    for d in grid.get_cells()[var[0]][var[1]]:
        copy_g = grid.copy()
        copy_g.get_cells()[var[0]][var[1]] = str(d)
        failure = ac3(copy_g, var)
        if not failure:
            # copy_g.print()
            rb = search(copy_g, var_selector)
            if rb[1] == True:
                # rb[0].print()
                return rb
            
                
    return grid, False

# file = open('tutorial_problem.txt', 'r')
# problems = file.readlines()
# for p in problems:
#     g = Grid()
#     g.read_file(p)
#     g.print()
#     pre_process_ac3(g)
#     g.print_domains()
#     grid = search(g, select_variable_mrv)
#     print(grid[0].is_solved())
#     grid[0].print()

    # 4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......


    # test your backtracking implementation without inference here
    # this test instance is only meant to help you debug your backtracking code
    # once you have implemented forward checking, it is fine to find a solution to this instance with inference




file = open('top95.txt', 'r')
problems = file.readlines()

mrv_running_times = []
fa_running_times = []

# running the search for each problem in top95 testing select_variable_fa
for p in problems:
    g = Grid()
    g.read_file(p)
    pre_process_ac3(g)
    start = time.time()
    grid = search(g, select_variable_fa)
    end = time.time()
    fa_running_times.append((end - start))
    print(grid[0].is_solved_deep())



# running the search for each problem in top95 testing select_variable_mrv
for p in problems:
    g = Grid()
    g.read_file(p)
    pre_process_ac3(g)
    start = time.time()
    grid = search(g, select_variable_mrv)
    end = time.time()
    mrv_running_times.append((end - start))
    print(grid[0].is_solved_deep())




plotter = PlotResults()
plotter.plot_results(mrv_running_times, fa_running_times,
"Running Time Backtracking (MRV)",
"Running Time Backtracking (FA)", "running_time")
    # test your backtracking implementation with inference here for instance grid_copy