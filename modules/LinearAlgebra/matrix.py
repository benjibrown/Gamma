import rich
import time
from rich import print as rprint
from rich.prompt import Prompt as input
from sploitkit import Module, Config, Option
from sympy import Matrix, sympify, det, solve_linear_system

timestamp = time.strftime('%H:%M:%S')

prefixes = {
    "general": "[bold blue][*][/bold blue]",
    "error": "[bold red][!][/bold red]",
    "success": "[bold green][+][/bold green]",
    "input": "[bold blue][>][/bold blue]",
    "info": "[bold cyan][i][/bold cyan]",
    "question": "[bold yellow][?][/bold yellow]",
    "timestamp": f"[bold magenta][{timestamp}][/bold magenta]",
}

class matrix(Module):
    """Matrix operations calculator
    
    Author: benjibrown
    Version: 1.0
    """
    config = Config({
        Option(
            'OPERATION',
            "Operation to perform (add, multiply, determinant, inverse, system)",
            True,
        ): None
    })

    def get_matrix(self, prompt):
        """Helper function to get matrix input"""
        rprint(f"{prefixes['info']} Enter matrix row by row")
        rprint(f"{prefixes['general']} Format: separate elements by spaces, rows by enter")
        rprint(f"{prefixes['general']} Example:")
        rprint(f"{prefixes['general']} 1 2 3")
        rprint(f"{prefixes['general']} 4 5 6")
        rprint(f"{prefixes['general']} 7 8 9")
        rprint(f"{prefixes['general']} Enter blank line when done")
        
        rows = []
        while True:
            row = input.ask(f"{prefixes['input']} {prompt}").strip()
            if not row:
                break
            try:
                rows.append([float(x) for x in row.split()])
                if rows[-1] == []:
                    rows.pop()
            except ValueError:
                rprint(f"{prefixes['error']} Invalid input, try again")
                rows = []
                continue
        return Matrix(rows)

    def run(self):
        title = "Matrix Operations Calculator"
        author = "Author: @benjibrown"
        version = "1.0"
        rprint(f"{prefixes['info']} {title}\n{prefixes['info']} {author}\n{prefixes['info']} Version: {version}")
        try:
            operations = ['add', 'multiply', 'determinant', 'inverse', 'system']
            if self.config['OPERATION'] is not None:
                operation = self.config['OPERATION'].lower()
                rprint(f"{prefixes['info']} Using operation from config")
                rprint(f"{prefixes['general']} Operation: {operation}")
            else:
                rprint(f"{prefixes['info']} Available operations: {', '.join(operations)}")
                operation = input.ask(f"{prefixes['input']} Enter operation:").lower()
            
            if operation not in operations:
                rprint(f"{prefixes['error']} Invalid operation. Choose from: {', '.join(operations)}")
                return

            if operation == 'add':
                matrix1 = self.get_matrix("Enter first matrix:")
                matrix2 = self.get_matrix("Enter second matrix:")
                if matrix1.shape != matrix2.shape:
                    rprint(f"{prefixes['error']} Matrices must have same dimensions")
                    return
                result = matrix1 + matrix2
                rprint(f"{prefixes['success']} Result:")
                rprint(f"{prefixes['general']} {result}")

            elif operation == 'multiply':
                matrix1 = self.get_matrix("Enter first matrix:")
                matrix2 = self.get_matrix("Enter second matrix:")
                if matrix1.shape[1] != matrix2.shape[0]:
                    rprint(f"{prefixes['error']} Invalid dimensions for multiplication")
                    return
                result = matrix1 * matrix2
                rprint(f"{prefixes['success']} Result:")
                rprint(f"{prefixes['general']} {result}")

            elif operation == 'determinant':
                matrix = self.get_matrix("Enter matrix:")
                if matrix.shape[0] != matrix.shape[1]:
                    rprint(f"{prefixes['error']} Matrix must be square")
                    return
                result = matrix.det()
                rprint(f"{prefixes['success']} Determinant: {result}")

            elif operation == 'inverse':
                matrix = self.get_matrix("Enter matrix:")
                if matrix.shape[0] != matrix.shape[1]:
                    rprint(f"{prefixes['error']} Matrix must be square")
                    return
                if matrix.det() == 0:
                    rprint(f"{prefixes['error']} Matrix is not invertible (determinant = 0)")
                    return
                result = matrix.inv()
                rprint(f"{prefixes['success']} Inverse:")
                rprint(f"{prefixes['general']} {result}")

            elif operation == 'system':
                rprint(f"{prefixes['info']} Enter augmented matrix (coefficients | constants)")
                matrix = self.get_matrix("Enter row:")
                result = matrix.rref()
                rprint(f"{prefixes['success']} Solution:")
                rprint(f"{prefixes['general']} {result[0]}")
            
            rprint(f"{prefixes['timestamp']} Process complete.")
        except ValueError as ve:
            rprint(f"{prefixes['error']} Invalid input: {ve}")
        except Exception as e:
            rprint(f"{prefixes['error']} An error occurred: {e}")