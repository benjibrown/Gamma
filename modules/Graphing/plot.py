
import rich
import time
from rich import print as rprint
from rich.prompt import Prompt as input
from sploitkit import Module, Config, Option
import plotext as plt
import numpy as np

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

class plot(Module):
    """Plots up to 4 functions in the terminal"""

    def run(self):
        title = "Terminal Graph Plotter"
        author = "Author: @benjibrown & Gemini"
        version = "1.0"
        rprint(f"{prefixes['info']} {title}\n{prefixes['info']} {author}\n{prefixes['info']} Version: {version}")
        print("\n")

        functions = []
        for i in range(4):
            func_str = input.ask(f"{prefixes['input']} Enter function {i+1} (or press Enter to finish)")
            if not func_str:
                break
            functions.append(func_str)

        if not functions:
            rprint(f"{prefixes['erorr']} No functions entered.")
            return

        try:
            x = np.linspace(-10, 10, 500)
            plt.clt()
            plt.clc()
            plt.figsize(100, 30)
            plt.axes_color("white")
            plt.grid(True)

            for func_str in functions:
                # Sanitize the function string for security
                safe_dict = {
                    'np': np,
                    'x': x,
                    'sin': np.sin,
                    'cos': np.cos,
                    'tan': np.tan,
                    'sqrt': np.sqrt,
                    'exp': np.exp,
                    'log': np.log,
                    'log10': np.log10,
                }
                y = eval(func_str.replace('^', '**'), {"__builtins__": {}}, safe_dict)
                plt.plot(x, y, label=func_str)

            plt.title("Function Plot")
            plt.xlabel("x")
            plt.ylabel("y")
            plt.show()
            rprint(f"{prefixes['timestamp']} Process complete.")

        except Exception as e:
            rprint(f"{prefixes['erorr']} An error occurred: {e}")
