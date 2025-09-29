import rich
import time
from rich import print as rprint
from rich.prompt import Prompt as input
from sploitkit import Module, Config, Option
from sympy import symbols, limit, sympify, Symbol, oo

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

class limits(Module):
    """Limit calculator for various expressions
    
    Author: benjibrown
    Version: 1.0
    """
    config = Config({
        Option(
            'FUNCTION',
            "Function to find limit of - write powers as '**', e.g. x**2 + 3*x",
            True,
        ): None,
        Option(
            'VARIABLE',
            "Variable to take limit with respect to (default: x)",
            True,
        ): "x",
        Option(
            'POINT',
            "Point to take limit at (use 'oo' for infinity)",
            True,
        ): None,
        Option(
            'DIRECTION',
            "Direction to take limit from (-1 for left, 1 for right, None for both)",
            True,
        ): None
    })

    def run(self):
        title = "Limit Calculator (supports trig, polynomials, exponentials, etc.)"
        author = "Author: @benjibrown"
        version = "1.0"
        rprint(f"{prefixes['info']} {title}\n{prefixes['info']} {author}\n{prefixes['info']} Version: {version}")
        try:
            if self.config['FUNCTION'] is not None:
                expr_str = self.config['FUNCTION']
                rprint(f"{prefixes['info']} Using function from config")
                rprint(f"{prefixes['general']} Function: {expr_str}")
            else:
                expr_str = input.ask(f"{prefixes['input']} Enter function to find limit of (e.g. sin(x)/x):")
            
            if self.config['VARIABLE'] is not None:
                var_str = self.config['VARIABLE']
                rprint(f"{prefixes['info']} Using variable from config")
                rprint(f"{prefixes['general']} Variable: {var_str}")
            else:
                var_str = input.ask(f"{prefixes['input']} Enter the variable (default: x):", default="x")
            
            if self.config['POINT'] is not None:
                point_str = self.config['POINT']
                rprint(f"{prefixes['info']} Using point from config")
                rprint(f"{prefixes['general']} Point: {point_str}")
            else:
                point_str = input.ask(f"{prefixes['input']} Enter the point to find limit at (use 'oo' for infinity):")
            
            if self.config['DIRECTION'] is not None:
                direction = self.config['DIRECTION']
                if direction is not None:
                    direction = int(direction)
                rprint(f"{prefixes['info']} Using direction from config: {direction}")
            else:
                rprint(f"{prefixes['info']} Direction options:")
                rprint(f"{prefixes['general']} -1: Approach from left (x → point from smaller values)")
                rprint(f"{prefixes['general']}  1: Approach from right (x → point from larger values)")
                rprint(f"{prefixes['general']} blank: Approach from both sides")
                dir_str = input.ask(f"{prefixes['input']} Enter direction:", default="")
                direction = int(dir_str) if dir_str else None

            x = symbols(var_str)
            expr = sympify(expr_str)
            point = float('inf') if point_str.lower() == 'oo' else sympify(point_str)
            
            result = limit(expr, x, point, dir=direction)
            
            dir_text = {
                -1: "from left",
                1: "from right",
                None: ""
            }
            
            rprint(f"{prefixes['success']} lim({expr_str}) as {var_str} → {point_str} {dir_text[direction]} = {result}")
            rprint(f"{prefixes['timestamp']} Process complete.")
        except ValueError as ve:
            rprint(f"{prefixes['error']} Invalid input: {ve}")
        except Exception as e:
            rprint(f"{prefixes['error']} An error occurred: {e}")