
class SparseMatrix:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.data = {}  # {(row, col): value}

    @classmethod
    def from_file(cls, filepath):
        try:
            with open(filepath, 'r') as file:
                lines = file.readlines()
                rows_line = lines[0].strip()
                cols_line = lines[1].strip()

                if not rows_line.startswith("rows=") or not cols_line.startswith("cols="):
                    raise ValueError("Input file has wrong format")

                num_rows = int(rows_line.split("=")[1])
                num_cols = int(cols_line.split("=")[1])

                matrix = cls(num_rows, num_cols)

                for line in lines[2:]:
                    line = line.strip()
                    if not line:
                        continue  # Ignore empty lines
                    if not (line.startswith("(") and line.endswith(")")):
                        raise ValueError("Input file has wrong format")
                    content = line[1:-1].split(",")
                    if len(content) != 3:
                        raise ValueError("Input file has wrong format")
                    try:
                        r, c, v = int(content[0]), int(content[1]), int(content[2])
                        matrix.set_element(r, c, v)
                    except ValueError:
                        raise ValueError("Input file has wrong format")
            return matrix
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{filepath}' not found.")

    def set_element(self, row, col, value):
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]

    def get_element(self, row, col):
        return self.data.get((row, col), 0)

    def __add__(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix dimensions must match for addition.")
        result = SparseMatrix(self.num_rows, self.num_cols)
        keys = set(self.data.keys()).union(other.data.keys())
        for key in keys:
            value = self.get_element(*key) + other.get_element(*key)
            if value != 0:
                result.set_element(key[0], key[1], value)
        return result

    def __sub__(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix dimensions must match for subtraction.")
        result = SparseMatrix(self.num_rows, self.num_cols)
        keys = set(self.data.keys()).union(other.data.keys())
        for key in keys:
            value = self.get_element(*key) - other.get_element(*key)
            if value != 0:
                result.set_element(key[0], key[1], value)
        return result

    def __matmul__(self, other):
        if self.num_cols != other.num_rows:
            raise ValueError("Matrix dimensions not compatible for multiplication.")
        result = SparseMatrix(self.num_rows, other.num_cols)
        for (i, k1), v1 in self.data.items():
            for j in range(other.num_cols):
                v2 = other.get_element(k1, j)
                if v2 != 0:
                    result.set_element(i, j, result.get_element(i, j) + v1 * v2)
        return result

    def to_string(self):
        output = [f"rows={self.num_rows}", f"cols={self.num_cols}"]
        for (row, col), value in sorted(self.data.items()):
            output.append(f"({row}, {col}, {value})")
        return "\n".join(output)


def main():
    print("Sparse Matrix Operation Tool")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")

    choice = input("Enter choice (1/2/3): ").strip()

    path1 = input("Enter path to first matrix file: ").strip()
    path2 = input("Enter path to second matrix file: ").strip()

    try:
        mat1 = SparseMatrix.from_file(path1)
        mat2 = SparseMatrix.from_file(path2)

        if choice == '1':
            result = mat1 + mat2
            print("\nResult of Addition:")
        elif choice == '2':
            result = mat1 - mat2
            print("\nResult of Subtraction:")
        elif choice == '3':
            result = mat1 @ mat2
            print("\nResult of Multiplication:")
        else:
            print("Invalid choice.")
            return

        print(result.to_string())

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()