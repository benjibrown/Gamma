import rich
import time
from rich import print as rprint
from rich.prompt import Prompt as input
from sploitkit import Module, Config, Option
from sympy import symbols, integrate, sympify, Symbol

timestamp = time.strftime('%H:%M:%S')

prefixes = {
    "general": "[bold blue][*][/bold blue]",
    "erorr": "[bold red][!][/bold red]",
    "success": "[bold green][+][/bold green]",
    "input": "[bold blue][>][/bold blue]",
    "info": "[bold cyan][;][/bold cyan]",
    "question": "[bold yellow][?][/bold yellow]",
    "timestamp": f"[bold magenta][{timestamp}][/bold magenta]",
}

class defintegral(Module):
    """Definite integral solver for various expressions
    
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
            'UPPER_LIMIT',
            "Upper limit of integration",
            True,
        ): None,     
        Option(
            'LOWER_LIMIT',
            "Lower limit of integration",
            True,
        ): None,
        Option(
            'VARIABLE',
            "Variable of integration (default: x)",
            True,
        ): "x",               
 
    })
    def run(self):
        title = "Definite Integral Solver (supports trig, polynomials, exponentials, etc.)"
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
            try:
                expr = sympify(expr_str)
            except Exception:
                rprint(f"{prefixes['erorr']} Invalid expression. Please enter a valid mathematical expression.")
                return

            # Get and validate the upper limit
            if self.config['UPPER_LIMIT'] is not None:
                upper_limit_str = self.config['UPPER_LIMIT']
                rprint(f"{prefixes['info']} Using upper limit from config: {upper_limit_str}")
            else:
                upper_limit_str = input.ask(f"{prefixes['input']} Enter the upper limit of integration:")
            try:
                upper_limit = float(upper_limit_str)
            except Exception:
                rprint(f"{prefixes['erorr']} Upper limit must be a valid number.")
                return

            # Get and validate the lower limit
            if self.config['LOWER_LIMIT'] is not None:
                lower_limit_str = self.config['LOWER_LIMIT']
                rprint(f"{prefixes['info']} Using lower limit from config: {lower_limit_str}")
            else:
                lower_limit_str = input.ask(f"{prefixes['input']} Enter the lower limit of integration:")
            try:
                lower_limit = float(lower_limit_str)
            except Exception:
                rprint(f"{prefixes['erorr']} Lower limit must be a valid number.")
                return

            # Get and validate the variable
            if self.config['VARIABLE']:
                var_str = self.config['VARIABLE']
                rprint(f"{prefixes['info']} Using variable from config: {var_str}")
            else:
                var_str = input.ask(f"{prefixes['input']} Enter the variable of integration (default: x):", default="x")
            if not var_str.isidentifier():
                rprint(f"{prefixes['erorr']} Variable name must be a valid identifier (e.g. x, y).")
                return
            x = symbols(var_str)

            # Compute the definite integral
            try:
                result = integrate(expr, (x, lower_limit, upper_limit))
            except Exception:
                rprint(f"{prefixes['erorr']} Could not compute the integral. Please check your input.")
                return
            rprint(f"{prefixes['success']} ∫ {expr_str} d{var_str} = {result}")
            rprint(f"{prefixes['timestamp']} Process complete.")
        except Exception as e:
            rprint(f"{prefixes['erorr']} An error occurred: {e}")