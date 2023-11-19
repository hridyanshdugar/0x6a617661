
from manim import *


class MatrixMultiplication(Scene):

    def construct(self):
        # Define matrices A and B
        matrixA = Matrix([[1, 2], [3, 4]], left_bracket="(", right_bracket=")")
        matrixB = Matrix([[5, 6], [7, 8]], left_bracket="(", right_bracket=")")

        # Position matrices
        matrixA.move_to(LEFT * 4)
        matrixB.move_to(RIGHT * 4)

        # Display matrices
        self.play(Write(matrixA), Write(matrixB))
        self.wait(1)

        # Perform and display multiplication
        result_matrix = self.multiply_matrices(matrixA, matrixB)

        # Check if result_matrix is not None
        if result_matrix:
            # Display resulting matrix
            result_matrix.move_to(RIGHT * 2)
            self.play(ReplacementTransform(matrixB, result_matrix))
            self.wait(2)
        else:
            # Display an error message or handle the None case appropriately
            self.add(Text("Matrix multiplication not possible",
                     color=RED).to_edge(UP))

    def multiply_matrices(self, matrixA, matrixB):
        # Manually calculate the dimensions of the matrices
        rowsA = len(matrixA.get_entries()
                    ) // len(matrixA.get_brackets()[0].submobjects)
        colsA = len(matrixA.get_entries()) // rowsA
        rowsB = len(matrixB.get_entries()
                    ) // len(matrixB.get_brackets()[0].submobjects)
        colsB = len(matrixB.get_entries()) // rowsB

    # Ensure matrices can be multiplied
        if colsA != rowsB:
            self.add(Text("Matrices cannot be multiplied!").set_color(RED))
            return None

    # ... rest of the function ...

    # Initialize the resulting matrix with placeholders
        result = [["" for _ in range(colsB)] for _ in range(rowsA)]
        result_matrix = Matrix(result, left_bracket="[", right_bracket="]")

        # Position the resulting matrix
        result_matrix.next_to(matrixB, RIGHT, buff=1)

        # Display the initial result matrix with placeholders
        self.play(Write(result_matrix))
        self.wait(1)

        # Iterate through each cell of the result matrix
        for i in range(rowsA):
            for j in range(colsB):
                # Calculate the sum of products for this cell
                cell_sum = 0
                sum_expression = VGroup()
                for k in range(colsA):
                    # Highlight the current elements
                    elemA = matrixA.get_entries()[i * colsA + k]
                    elemB = matrixB.get_entries()[k * colsB + j]
                    self.play(elemA.animate.set_color(YELLOW),
                              elemB.animate.set_color(YELLOW))
                    self.wait(0.5)

                    # Calculate product and add to the sum
                    product = elemA.get_value() * elemB.get_value()
                    cell_sum += product

                    # Create a visual representation of the product
                    product_mob = MathTex(str(product))
                    if sum_expression.submobjects:
                        product_mob.next_to(sum_expression, RIGHT)
                    else:
                        product_mob.next_to(result_matrix, DOWN)

                    sum_expression.add(product_mob)
                    self.play(Write(product_mob))
                    self.wait(0.5)

                    # Unhighlight the elements
                    self.play(elemA.animate.set_color(WHITE),
                              elemB.animate.set_color(WHITE))

                # Update the cell in the result matrix
                result_cell = MathTex(str(cell_sum))
                result_cell.move_to(result_matrix.get_entries()[i * colsB + j])
                self.play(Transform(result_matrix.get_entries()
                          [i * colsB + j], result_cell))
                self.wait(1)
        return result_matrix


# Additional functions for animations can be added here
