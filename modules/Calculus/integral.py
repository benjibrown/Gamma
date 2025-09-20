import rich
import time
from rich import print as rprint
from rich.prompt import Prompt as input
from sploitkit import Module
from sympy import symbols, integrate, sympify, Symbol

timestamp = time.strftime('%H:%M:%S')

prefixes = {
    "general": "[bold blue][*][/bold blue]",
    "erorr": "[bold red][!][/bold red]",
    "success": "[bold green][+][/bold green]",
    "input": "[bold blue][>][/bold blue]",
    "info": "[bold cyan][i][/bold cyan]",
    "question": "[bold yellow][?][/bold yellow]",
    "timestamp": f"[bold magenta][{timestamp}][/bold magenta]",
}

class solveintegral(Module):
    """Indefinite integral solver for various expressions
    
    Author: benjibrown
    Version: 1.0
    """

    def run(self):
        title = "Indefinite Integral Solver (supports trig, polynomials, exponentials, etc.)"
        author = "Author: @benjibrown"
        version = "1.0"
        rprint(f"{prefixes['info']} {title}\n{prefixes['info']} {author}\n{prefixes['info']} Version: {version}")
        try:
            expr_str = input.ask(f"{prefixes['input']} Enter an expression to integrate (e.g. sin(x), x**2 + 3*x):")
            var_str = input.ask(f"{prefixes['input']} Enter the variable of integration (default: x):", default="x")
            x = symbols(var_str)
            expr = sympify(expr_str)
            integral = integrate(expr, x)
            result = integral + Symbol('C')
            rprint(f"{prefixes['success']} ∫ {expr_str} d{var_str} = {result}")
            rprint(f"{prefixes['timestamp']} Process complete.")
        except Exception as e:
            rprint(f"{prefixes['erorr']} An error occurred: {e}")