import rich
import time
from rich import print as rprint
from rich.prompt import Prompt as input
from sploitkit import Module, Config, Option
from sympy import symbols, integrate, sympify, Symbol, solve

timestamp = time.strftime('%H:%M:%S')

prefixes = {
    "general": "[bold blue][*][/bold blue]",
    "error": "[bold red][!][/bold red]",
    "success": "[bold green][+][/bold green]",
    "input": "[bold blue][>][/bold blue]",
    "info": "[bold cyan1][;][/bold cyan1]",
    "question": "[bold yellow][?][/bold yellow]",
    "timestamp": f"[bold magenta][{timestamp}][/bold magenta]",
}

class indefintegral(Module):
    """Indefinite integral solver for various expressions
    
    Author: benjibrown
    Version: 1.0
    """
    config = Config({
        Option(
            'INTEGRAL',
            "Integral to compute - write powers as '**', e.g. x**2 + 3**x",
            True,
        ): None,
        Option(
            'VARIABLE',
            "Variable of integration (default: x)",
            True,
        ): "x",
    })
    def run(self):
        title = "Indefinite Integral Solver (supports trig, polynomials, exponentials, etc.)"
        author = "Author: @benjibrown"
        version = "1.0"
        rprint(f"{prefixes['info']} {title}\n{prefixes['info']} {author}\n{prefixes['info']} Version: {version}")
        print("\n")
        try:
            # Get and validate the expression
            if self.config['INTEGRAL'] is not None:
                expr_str = self.config['INTEGRAL']
                rprint(f"{prefixes['info']} Using integral from config: {expr_str}")
            else:    
                expr_str = input.ask(f"{prefixes['input']} Enter an expression to integrate (e.g. sin(x), x**2 + 3*x):")
            if self.config['VARIABLE'] is not None:
                var_str = self.config['VARIABLE']
                rprint(f"{prefixes['info']} Using variable of integration from config: {var_str}")
            else:
                var_str = input.ask(f"{prefixes['input']} Enter the variable of integration (default: x):", default="x")
            x = symbols(var_str)
            expr = sympify(expr_str)
            integral = integrate(expr, x)
            result = str(integral) + " + C"
            rprint(f"{prefixes['success']} ∫ {expr_str} d{var_str} = {result}")
            rprint(f"{prefixes['timestamp']} Process complete.")
        except Exception as e:
            rprint(f"{prefixes['error']} An error occurred: {e}")
   