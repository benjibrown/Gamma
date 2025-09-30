import rich
import time
from rich import print as rprint
from rich.prompt import Prompt as input
from sploitkit import Module, Config, Option
from sympy import Matrix, sympify, sqrt

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

class vector(Module):
    """Vector operations calculator
    
    Author: benjibrown
    Version: 1.0
    """
    config = Config({
        Option(
            'OPERATION',
            "Operation to perform (add, dot, cross, magnitude, angle)",
            True,
        ): None
    })

    def get_vector(self, prompt):
        """Helper function to get vector input"""
        while True:
            try:
                vec_str = input.ask(f"{prefixes['input']} {prompt} (e.g., 1 2 3):")
                return Matrix([float(x) for x in vec_str.split()])
            except ValueError:
                rprint(f"{prefixes['error']} Invalid input, try again")

    def run(self):
        title = "Vector Operations Calculator"
        author = "Author: @benjibrown"
        version = "1.0"
        rprint(f"{prefixes['info']} {title}\n{prefixes['info']} {author}\n{prefixes['info']} Version: {version}")
        try:
            operations = ['add', 'dot', 'cross', 'magnitude', 'angle']
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
                vec1 = self.get_vector("Enter first vector")
                vec2 = self.get_vector("Enter second vector")
                if vec1.shape != vec2.shape:
                    rprint(f"{prefixes['error']} Vectors must have same dimensions")
                    return
                result = vec1 + vec2
                rprint(f"{prefixes['success']} Result:")
                rprint(f"{prefixes['general']} {result.T}")

            elif operation == 'dot':
                vec1 = self.get_vector("Enter first vector")
                vec2 = self.get_vector("Enter second vector")
                if vec1.shape != vec2.shape:
                    rprint(f"{prefixes['error']} Vectors must have same dimensions")
                    return
                result = vec1.dot(vec2)
                rprint(f"{prefixes['success']} Dot product: {result}")

            elif operation == 'cross':
                vec1 = self.get_vector("Enter first vector")
                vec2 = self.get_vector("Enter second vector")
                if vec1.shape != (3, 1) or vec2.shape != (3, 1):
                    rprint(f"{prefixes['error']} Vectors must be 3-dimensional")
                    return
                result = vec1.cross(vec2)
                rprint(f"{prefixes['success']} Cross product:")
                rprint(f"{prefixes['general']} {result.T}")

            elif operation == 'magnitude':
                vec = self.get_vector("Enter vector")
                result = sqrt(sum(x*x for x in vec))
                rprint(f"{prefixes['success']} Magnitude: {result}")

            elif operation == 'angle':
                vec1 = self.get_vector("Enter first vector")
                vec2 = self.get_vector("Enter second vector")
                if vec1.shape != vec2.shape:
                    rprint(f"{prefixes['error']} Vectors must have same dimensions")
                    return
                dot_product = vec1.dot(vec2)
                mag1 = sqrt(sum(x*x for x in vec1))
                mag2 = sqrt(sum(x*x for x in vec2))
                cos_angle = dot_product/(mag1 * mag2)
                angle = float(cos_angle.acos())
                rprint(f"{prefixes['success']} Angle: {angle} radians")
                rprint(f"{prefixes['general']} Angle: {angle * 180/3.14159:.2f} degrees")
            
            rprint(f"{prefixes['timestamp']} Process complete.")
        except ValueError as ve:
            rprint(f"{prefixes['error']} Invalid input: {ve}")
        except Exception as e:
            rprint(f"{prefixes['error']} An error occurred: {e}")