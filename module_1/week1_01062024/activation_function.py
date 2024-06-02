import math

def is_number(number):
    try:
        float(number)
    except ValueError:
        return False
    return True

def activation_function(func_name, x):
    x = float(x)
    if func_name == 'sigmoid':
        print(f'sigmoid: f({x}) = {1/(1+math.e**-x)}')
    elif func_name == 'relu':
        print(f'relu: f({x}) = {max(0, x)}')
    elif func_name == 'elu':
        alpha = 0.01
        print(f'elu: f({x}) = {max(x, alpha*(math.e**x - 1))}')
    else:
        print(f'{func_name} is not supported')
    
if __name__ == "__main__":
    number = input('Input x = ')
    if not is_number(number):
        print('x must be a number')
    else:
        func_name = input('Input activation Function (sigmoid | relu | elu): ')
        activation_function(func_name, number)