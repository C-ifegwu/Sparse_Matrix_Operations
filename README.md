Data_Structure_And_Algorithms By Chibueze Victor Ifegwu
Sparse Matrix Operations
Overview
This project implements Sparse Matrix Operations in Python. The program supports:

Reading sparse matrices from text files
Performing addition, subtraction, and multiplication on sparse matrices
Storing results in an output file
The SparseMatrix class efficiently stores and manipulates matrices using a dictionary representation to save memory by only keeping track of nonzero elements.

Features
Sparse Matrix Representation: Stores nonzero values using a dictionary
Matrix Operations: Supports addition, subtraction, and multiplication
File Input and Output: Reads matrix data from files and saves results to files
Command-Line Interface: Users can interactively provide input file paths and choose operations
Project Structure
Sparse_matrix/
│── code/
│   ├── src/
│   │   ├── my_sparse_matrix.py  # Entry point of the program

│── sample_inputs/
│   ├── matrix1.txt  # Sample input matrix
│   ├── matrix2.txt # Another sample input matrix
│
│── result.txt  # File where the output matrix is stored
│── README.md  # Project documentation
Installation & Requirements
This project requires Python 3.7+.

1️⃣ Clone the Repository
https://github.com/C-ifegwu/Stress_matrix.git
cd sparse-matrix/code/src
2️⃣ Run the Program
python my_sparse_matrix.py
How to Use the Program
**Run **`` and enter the file paths for two matrices.
Choose an operation:
1 for addition
2 for subtraction
3 for multiplication
View the result on the console or in the output file.
Example input files (e.g., matrixfile1.txt):

rows=3
cols=3
(0,0,5)
(1,1,8)
(2,2,3)
Implementation Details
SparseMatrix Class
Stores elements in a dictionary {(row, col): value}
Handles file input/output with save_to_file() and _load_from_file()
Operations Implemented in operations.py
add_matrices(mat1, mat2): Adds two matrices
subtract_matrices(mat1, mat2): Subtracts two matrices
multiply_matrices(mat1, mat2): Multiplies two matrices
Example Output
Sparse Matrix Operations
Enter path for first matrix file: sample_inputs/matrixfile1.txt
Enter path for second matrix file: sample_inputs/matrixfile2.txt
Choose operation:
1. Addition
2. Subtraction
3. Multiplication
Enter your choice (1/2/3): 1
✅ Output saved toFinally_the result.txt
