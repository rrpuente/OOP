
def factorial(n):
    f = 1
    for i in range (1,n+1):
        f = f * i
    return f

def binomial_coeficient(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))

def add_spaces_to_val(val):
    sval = str(val)
    if len(sval) == 1:
        sval = ' ' + sval + ' '
    elif len(sval) == 2:
        sval = sval + ' '
    return sval

def print_pascal_triangle(n):
    space = '   '
    
    for row in range(n):
        # row i have i+1 cols
        left_spaces = space * (n-row)
        print(left_spaces, end=space)
        for col in range(row+1):
            #calculate the value for col 
            val = int(binomial_coeficient(row, col))
            print ( add_spaces_to_val(val), end=space)
        print('') # change to the new line


if __name__ == '__main__':
    n = 5
    print_pascal_triangle(n)
