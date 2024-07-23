import numpy as np
import sympy as sym
from fpdf import FPDF

# save FPDF() class into a
# variable pdf
pdf = FPDF()
 
# Add a page
pdf.add_page()
pdf.add_page()

pdf.set_font("Arial", size = 15)

def print(a):
    i = 0
    i += 1
    pdf.cell(200, 10, txt = a,
         ln = i, align = 'L')

# Task 1
print('Cell 1: Augumented Matrix')
A = np.array([[1,2,-3],[2,5,-8],[3,8,-13]])
B = np.array([[1],[4],[7]])

augAB = np.concatenate((A,B), axis=1)
print (f'The augumented matrix:\n{augAB}\n')

# Task 2
print('Cell 2: RREF')
RREF = sym.Matrix(augAB).rref() 
print(f'The Reduced Row Echelon Form\n{RREF}\n') 

# Task 3
print('Cell 3: Manual operations') 
print('The system is consistent\nPivots = (1,1), (2,2)\nx1 and x2 are the basic variables\nx3 is the free variable\n')

# Task 4
print('Cell 4: Solution to System of Equations') 
print('x1 = -x3-3\nx2 = 2+2x3\nx3 = free variable\n')

# Task 5
print('Cell 5: Numerical solution and Verification')
x3 = 6
x1 = -3-x3
x2 = 2+2*x3
sol_vec1 = np.array([[x1],[x2],[x3]])
s1 = np.matmul(A, sol_vec1)
print(f'Solution vector 1:\n{sol_vec1}')
print(f'Solution vector 1 product:\n{s1}')
x3 = 0
x1 = -3-x3
x2 = 2+2*x3
sol_vec2 = np.array([[x1],[x2],[x3]])  
s2 = np.matmul(A, sol_vec2)
print(f'Solution vector 2:\n{sol_vec2}')
print(f'Solution vector 2 product:\n{s2}\n')
## check if the solution is correct manually by comparing to B

# Task 6 
print('Cell 6: Getting RREF')
print(f'A1 =\n{augAB}')
A1_row1 = augAB[0:1] # First dimension: row, index [0,1), which is the first row
print(f'A1_row1: {A1_row1}')
A1_row2 = augAB[1:2] # First dimension: row, index [1,2), which is the second row
print(f'A1_row2: {A1_row2}')
A1_row3 = augAB[2:3] # First dimension: row, index [2,3), which is the third row
print(f'A1_row3: {A1_row3}')

'''
subtract row 1 from row 2 and 2 with appropriate coefficients to make the first column a
pivot col
'''
A1_row3 = 2*A1_row2-A1_row3
A1_row2 = A1_row2-2*A1_row1
A2 = np.concatenate((A1_row1, A1_row2, A1_row3), axis=0) #
print(f'A2 =\n{A2}')
A2_row1 = A2[0:1] # First dimension: row, index [0,1), which is the first row
print(f'A2_row1: {A2_row1}')
A2_row2 = A2[1:2] # First dimension: row, index [1,2), which is the second row
print(f'A2_row2: {A2_row2}')
A2_row3 = A2[2:3] # First dimension: row, index [2,3), which is the third row
print(f'A2_row3: {A2_row3}')

A2_row3 = A2_row3-A1_row1
A2_row1 = A2_row1-2*A1_row2
A3 = np.concatenate((A2_row1, A2_row2, A2_row3), axis=0) #
print(f'Reduced Row Echelon Form =\n{A3}')

pdf.output("practice.pdf")

