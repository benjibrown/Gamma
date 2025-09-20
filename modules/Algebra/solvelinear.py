import rich
import time
from rich import print as rprint
from rich.prompt import Prompt as input
from sploitkit import Module, Config, Option, Command
from sympy import symbols, Eq, solve, sympify

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


class solvelinear(Module):
    # Coommand.set_style("module")
    """Basic solver for linear equations
    
    Author: benjibrown
    Version: 1.0
    """ 


    def run(self):

        title = "General linear equation solver (supports surds, exponents, etc.)"
        author = "Author:  @benjibrown"
        version = "1.1"
        rprint(f"{prefixes['info']} {title} \n {prefixes['info']} {author} \n {prefixes['info']} Version: {version}")
        try:
            eq_str = input.ask(f"{prefixes['input']} Enter a linear equation (e.g. 2*x + sqrt(3) = 5 - x)")
            if '=' not in eq_str:
                rprint(f"{prefixes['erorr']} Please enter an equation with '='.")
                return
            left, right = eq_str.split('=')
            x = symbols('x')
            eq = Eq(sympify(left), sympify(right))
            sol = solve(eq, x)
            if sol:
                rprint(f"{prefixes['success']} Solution(s) for x: {sol}")
            else:
                rprint(f"{prefixes['erorr']} No solution found.")
            rprint(f"{prefixes['timestamp']} Process complete.")
        except Exception as e:
            rprint(f"{prefixes['erorr']} An error occurred: {e}")
    


