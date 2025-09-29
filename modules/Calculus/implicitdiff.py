import rich
import time
from rich import print as rprint
from rich.prompt import Prompt as input
from sploitkit import Module, Config, Option
from sympy import symbols, diff, sympify, Symbol, solve

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

class implicitdiff(Module):
    """Implicit differentiation solver
    
    Author: benjibrown
    Version: 1.0
    """
    config = Config({
        Option(
            'EQUATION',
            "Equation to differentiate (e.g. x**2 + y**2 = 1)",
            True,
        ): None,
        Option(
            'RESPECT_TO',
            "Variable to differentiate with respect to (default: x)",
            True,
        ): "x"
    })

    def run(self):
        title = "Implicit Differentiation Solver"
        author = "Author: @benjibrown"
        version = "1.0"
        rprint(f"{prefixes['info']} {title}\n{prefixes['info']} {author}\n{prefixes['info']} Version: {version}")
        try:
            if self.config['EQUATION'] is not None:
                eq_str = self.config['EQUATION']
                rprint(f"{prefixes['info']} Using equation from config: {eq_str}")
            else:
                eq_str = input.ask(f"{prefixes['input']} Enter equation (e.g. x**2 + y**2 = 1):")
            
            if self.config['RESPECT_TO'] is not None:
                var_str = self.config['RESPECT_TO']
                rprint(f"{prefixes['info']} Using variable from config: {var_str}")
            else:
                var_str = input.ask(f"{prefixes['input']} Enter variable to differentiate with respect to (default: x):", default="x")

            # Parse equation
            if '=' not in eq_str:
                rprint(f"{prefixes['error']} Equation must contain '='")
                return
                
            left, right = eq_str.split('=')
            x, y = symbols('x y')
            expr = sympify(left) - sympify(right)
            
            # Calculate dy/dx using implicit differentiation
            dy_dx = -diff(expr, x) / diff(expr, y)
            
            rprint(f"{prefixes['success']} dy/dx = {dy_dx}")
            rprint(f"{prefixes['info']} This represents the derivative of y with respect to x")
            rprint(f"{prefixes['timestamp']} Process complete.")
        except ValueError as ve:
            rprint(f"{prefixes['error']} Invalid input: {ve}")
        except Exception as e:
            rprint(f"{prefixes['error']} An error occurred: {e}")