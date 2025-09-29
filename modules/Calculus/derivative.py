import rich
import time
from rich import print as rprint
from rich.prompt import Prompt as input
from sploitkit import Module, Config, Option
from sympy import symbols, diff, sympify, Symbol

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

class derivative(Module):
    """Derivative solver for various expressions
    
    Author: benjibrown
    Version: 1.0
    """
    config = Config({
        Option(
            'FUNCTION',
            "Function to differentiate - write powers as '**', e.g. x**2 + 3*x",
            True,
        ): None,
        Option(
            'VARIABLE',
            "Variable of differentiation (default: x)",
            True,
        ): "x",
        Option(
            'ORDER',
            "Order of derivative (default: 1)",
            True,
        ): 1
    })

    def run(self):
        title = "Derivative Solver (supports trig, polynomials, exponentials, etc.)"
        author = "Author: @benjibrown"
        version = "1.0"
        rprint(f"{prefixes['info']} {title}\n{prefixes['info']} {author}\n{prefixes['info']} Version: {version}")
        try:
            if self.config['FUNCTION'] is not None:
                expr_str = self.config['FUNCTION']
                rprint(f"{prefixes['info']} Using function from config")
                rprint(f"{prefixes['general']} Function: {expr_str}")
            else:    
                expr_str = input.ask(f"{prefixes['input']} Enter function to differentiate (e.g. sin(x), x**2 + 3*x):")           
            if self.config['VARIABLE'] is not None:
                var_str = self.config['VARIABLE']
                rprint(f"{prefixes['info']} Using variable from config")
                rprint(f"{prefixes['general']} Variable: {var_str}")
            else:
                var_str = input.ask(f"{prefixes['input']} Enter the variable (default: x):", default="x")
            
            if self.config['ORDER'] is not None:
                order = int(self.config['ORDER'])
                rprint(f"{prefixes['info']} Using order from config")
                rprint(f"{prefixes['general']} Order: {order}")
            else:
                order = int(input.ask(f"{prefixes['input']} Enter the order of derivative (default: 1):", default="1"))

            x = symbols(var_str)
            expr = sympify(expr_str)
            derivative = diff(expr, x, order)
            rprint(f"{prefixes['success']} d{order}/d{var_str}{order} ({expr_str}) = {derivative}")
            rprint(f"{prefixes['timestamp']} Process complete.")
        except ValueError as ve:
            rprint(f"{prefixes['error']} Invalid input: {ve}")
        except Exception as e:
            rprint(f"{prefixes['error']} An error occurred: {e}")