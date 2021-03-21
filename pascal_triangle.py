# return the factorial of n
def factorial(n):
    f = 1
    while n>1:
        f = f * n
        n = n -1
    return f
#return the binomial coeficient
def binomial_coeficient(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))

# here I will asume that the bigest value we are going to generate for the
#triangle has three digits. 
space = '   '
def add_spaces_to_val(val):
    sval = str(val)
    if len(sval) == 1:
        sval = ' ' + sval + ' '
    elif len(sval) == 2:
        sval = sval + ' '
    return sval

def print_pascal_triangle(n):
    for row in range(n):
        # row i have i+1 cols
        left_spaces = space * (n-row)
        # add spaces at the begening of the row to have the 
        #shape of the triangle
        print(left_spaces, end=space)
        for col in range(row+1):
            #calculate the value for col 
            val = int(binomial_coeficient(row, col))
            #adjust the number to three spaces
            print ( add_spaces_to_val(val), end=space)
        print('') # change to the new line


if __name__ == '__main__':
    n = 10
    print_pascal_triangle(n)
