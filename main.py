import numpy as np
from helper import get_formula, get_x, get_y, get_x_final, get_num_steps

def second_order():
    '''
    x (k+1) = xk + delta T * F2
    F1 = f(xk, tk)
    F2 = f(xk + delta t /2 * F1, tk + delta T/2)

    What we need:
    formul for dy/dx
    Starting x
    starting y
    number of steps
    fina x
    step size (can be found out using number of steps)
    
    '''
    dydx = get_formula()
    starting_x = (get_x())
    starting_y = (get_y())
    final_x = (get_x_final())
    num_steps = (get_num_steps())
    step_size = (final_x-starting_x)/num_steps
    for i in range(num_steps):
        #get the dy/dx at x1,y1 and use it to find dydx at x + delta t
        F1 = eval(dydx, {"np": np}, {"x": starting_x, "y":starting_y }) 
        F2 = eval(dydx, {"np": np}, {"x": starting_x + step_size/2, "y":starting_y + step_size/2 *F1})
        #use the value we get by finding the slope at x + delta t/2 to solve for an approximate solution for each time step
        starting_x=starting_x + step_size
        starting_y = starting_y + step_size*F2

    print(starting_y)
    print(starting_x)

def third_order():
    dydx = get_formula()
    starting_x = (get_x())
    starting_y = (get_y())
    final_x = (get_x_final())
    num_steps = (get_num_steps())
    step_size = (final_x-starting_x)/num_steps
    for i in range(num_steps):
        #evaluate f1, f2, f3, f4 (more detailed information given in a separate document)
        F1 = eval(dydx, {"np": np}, {"x": starting_x, "y":starting_y }) 
        F2 = eval(dydx, {"np": np}, {"x": starting_x + step_size/2, "y":starting_y + step_size/2 *F1})
        F3 = eval(dydx, {"np": np}, {"x": starting_x + step_size, "y":starting_y - step_size *F1 + 2* F2 * step_size})

        #implement fourth order runge_kutta
        starting_x=starting_x + step_size
        starting_y = starting_y + step_size*(F1+2*F2+2*F3)/6

    print(starting_y)
    print(starting_x)

def fourth_order():
    dydx = get_formula()
    starting_x = (get_x())
    starting_y = (get_y())
    final_x = (get_x_final())
    num_steps = (get_num_steps())
    step_size = (final_x-starting_x)/num_steps
    for i in range(num_steps):
        #evaluate f1, f2, f3, (more detailed information given in a separate document)
        F1 = eval(dydx, {"np": np}, {"x": starting_x, "y":starting_y }) 
        F2 = eval(dydx, {"np": np}, {"x": starting_x + step_size/2, "y":starting_y + step_size/2 *F1})
        F3 = eval(dydx, {"np": np}, {"x": starting_x + step_size/2, "y":starting_y + step_size/2 *F2})
        F4 = eval(dydx, {"np": np}, {"x": starting_x + step_size, "y":starting_y + step_size*F3})

        #implement fourth order runge_kutta
        starting_x=starting_x + step_size
        starting_y = starting_y + step_size*(F1+2*F2+2*F3+F4)/6

    print(starting_y)
    print(starting_x)





'''
Todo, def fifth order
'''





if __name__ == "__main__":
    fourth_order()





