#!/usr/bin/env python3

import os
import sys
import random
from pathlib import Path
from typing import List, Dict
import pyfiglet
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.tree import Tree
from rich import print as rprint
from rich.prompt import Prompt
from rich.syntax import Syntax

# Initialize rich console
console = Console()

# Bucky quotes for random display
BUCKY_QUOTES = [
    "You never change things by fighting the existing reality. To change something, build a new model that makes the existing model obsolete.",
    "We are called to be architects of the future, not its victims.",
    "The best way to predict the future is to design it.",
    "There is nothing in a caterpillar that tells you it's going to be a butterfly.",
    "Humanity is acquiring all the right technology for all the wrong reasons.",
]

class Explorer:
    def __init__(self):
        self.current_path = Path(".")
        self.history = []

    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('clear' if os.name == 'posix' else 'cls')

    def print_header(self):
        """Print the explorer header."""
        # Create ASCII art header
        header = pyfiglet.figlet_format("Bucky Explorer", font="slant")
        console.print(Panel(header, style="bold blue"))
        
        # Print random quote
        quote = random.choice(BUCKY_QUOTES)
        console.print(Panel(f"[italic yellow]'{quote}'[/]", style="blue"))

    def get_contents(self) -> Dict[str, List[Path]]:
        """Get directory contents."""
        contents = {"dirs": [], "md_files": [], "other_files": []}
        
        try:
            for item in sorted(self.current_path.iterdir()):
                if item.name.startswith('.'):
                    continue
                if item.is_dir():
                    contents["dirs"].append(item)
                elif item.suffix.lower() == '.md':
                    contents["md_files"].append(item)
                else:
                    contents["other_files"].append(item)
        except Exception as e:
            console.print(f"[red]Error reading directory: {e}[/]")
        
        return contents

    def show_tree(self, path: Path = None, tree: Tree = None) -> None:
        """Display directory structure as a tree."""
        if path is None:
            path = self.current_path
            tree = Tree(
                f"[bold blue]:file_folder: {path.name or 'Repository'}[/]",
                guide_style="bold bright_blue",
            )

        try:
            for entry in sorted(path.iterdir()):
                if entry.name.startswith('.'):
                    continue
                    
                if entry.is_dir():
                    branch = tree.add(f"[bold blue]:file_folder: {entry.name}[/]")
                    self.show_tree(entry, branch)
                else:
                    icon = "📄" if entry.suffix.lower() == '.md' else "📎"
                    tree.add(f"[green]{icon} {entry.name}[/]")
        except Exception:
            pass

    def view_file(self, path: Path) -> None:
        """View file contents with syntax highlighting."""
        try:
            content = path.read_text(encoding='utf-8')
            
            if path.suffix.lower() == '.md':
                md = Markdown(content)
                console.print(md)
            else:
                syntax = Syntax(content, "python", theme="monokai", line_numbers=True)
                console.print(syntax)
                
            console.print("\nPress Enter to continue...", style="bold yellow")
            input()
        except Exception as e:
            console.print(f"[red]Error reading file: {e}[/]")
            console.print("\nPress Enter to continue...", style="bold yellow")
            input()

    def browse(self) -> None:
        """Browse the current directory."""
        while True:
            self.clear_screen()
            contents = self.get_contents()
            
            # Show current path
            console.print(f"\n[bold blue]📍 Current:[/] {self.current_path}")
            
            # Show parent option if not in root
            if self.current_path != Path("."):
                console.print("\n[bold]⬆️  Parent Directory:[/]")
                console.print("0. [blue].. (Parent Directory)[/]")
            
            # Show directories
            if contents["dirs"]:
                console.print("\n[bold]📂 Directories:[/]")
                for i, d in enumerate(contents["dirs"], 1):
                    console.print(f"{i}. [blue]{d.name}/[/]")
            
            # Show markdown files
            if contents["md_files"]:
                console.print("\n[bold]📝 Documentation:[/]")
                start = len(contents["dirs"]) + 1
                for i, f in enumerate(contents["md_files"], start):
                    console.print(f"{i}. [green]{f.name}[/]")
            
            # Show other files
            if contents["other_files"]:
                console.print("\n[bold]📄 Other Files:[/]")
                start = len(contents["dirs"]) + len(contents["md_files"]) + 1
                for i, f in enumerate(contents["other_files"], start):
                    console.print(f"{i}. [yellow]{f.name}[/]")
            
            # Navigation options
            console.print("\n[bold]Navigation:[/]")
            console.print("b. [red]← Back to Menu[/]")
            
            choice = Prompt.ask("\nEnter your choice", default="b")
            
            if choice.lower() == 'b':
                break
                
            try:
                choice = int(choice)
                if choice == 0 and self.current_path != Path("."):
                    self.current_path = self.current_path.parent
                elif 1 <= choice <= len(contents["dirs"]):
                    self.current_path = contents["dirs"][choice - 1]
                else:
                    idx = choice - len(contents["dirs"]) - 1
                    if idx < len(contents["md_files"]):
                        self.view_file(contents["md_files"][idx])
                    else:
                        idx -= len(contents["md_files"])
                        if idx < len(contents["other_files"]):
                            self.view_file(contents["other_files"][idx])
            except ValueError:
                console.print("[red]Invalid choice. Please try again.[/]")
                continue

    def search(self) -> None:
        """Search for files."""
        term = Prompt.ask("\nEnter search term")
        
        with console.status("[bold green]Searching..."):
            results = []
            for path in self.current_path.rglob("*"):
                if path.is_file() and term.lower() in path.name.lower():
                    results.append(path)
        
        if results:
            console.print("\n[bold]🔍 Search Results:[/]")
            for i, path in enumerate(results, 1):
                console.print(f"{i}. [green]{path.relative_to(self.current_path)}[/]")
            
            choice = Prompt.ask("\nEnter number to view file (or Enter to skip)")
            if choice.isdigit() and 1 <= int(choice) <= len(results):
                self.view_file(results[int(choice) - 1])
        else:
            console.print(f"\n[yellow]No files found matching '{term}'[/]")
            console.print("\nPress Enter to continue...", style="bold yellow")
            input()

    def run(self) -> None:
        """Main program loop."""
        while True:
            try:
                self.clear_screen()
                self.print_header()
                
                console.print("\n[bold]🎯 Menu:[/]")
                console.print("1. [blue]📂 Browse Repository[/]")
                console.print("2. [blue]📖 View README[/]")
                console.print("3. [blue]🔍 Search Files[/]")
                console.print("4. [blue]🗺️  Show Repository Map[/]")
                console.print("5. [red]❌ Exit[/]")
                
                choice = Prompt.ask("\nEnter your choice", choices=["1", "2", "3", "4", "5"], default="1")
                
                if choice == "1":
                    self.browse()
                elif choice == "2":
                    if Path("README.md").exists():
                        self.view_file(Path("README.md"))
                    else:
                        console.print("[yellow]README.md not found![/]")
                        console.print("\nPress Enter to continue...", style="bold yellow")
                        input()
                elif choice == "3":
                    self.search()
                elif choice == "4":
                    self.clear_screen()
                    tree = Tree(
                        f"[bold blue]:file_folder: {self.current_path.name or 'Repository'}[/]",
                        guide_style="bold bright_blue",
                    )
                    self.show_tree(tree=tree)
                    console.print(tree)
                    console.print("\nPress Enter to continue...", style="bold yellow")
                    input()
                elif choice == "5":
                    self.clear_screen()
                    console.print(Panel.fit(
                        "[bold green]Thank you for exploring the Buckminster Fuller Knowledge Graph![/]\n" +
                        "[yellow]'The best way to predict the future is to design it.' - Bucky[/]"
                    ))
                    sys.exit(0)
                
            except KeyboardInterrupt:
                console.print("\n[yellow]Exiting gracefully...[/]")
                sys.exit(0)
            except Exception as e:
                console.print(f"[red]An error occurred: {e}[/]")
                console.print("\nPress Enter to continue...", style="bold yellow")
                input()

if __name__ == "__main__":
    try:
        # Ensure we're in the correct directory
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        explorer = Explorer()
        explorer.run()
    except Exception as e:
        console.print(f"[red]Failed to start: {e}[/]")
        sys.exit(1) 