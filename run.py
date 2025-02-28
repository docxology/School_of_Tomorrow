#!/usr/bin/env python3

import os
import sys
import time
import random
import textwrap
from typing import List, Dict, Any
import re
from pathlib import Path

# ANSI color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'

# Fun Bucky quotes
BUCKY_QUOTES = [
    "You never change things by fighting the existing reality. To change something, build a new model that makes the existing model obsolete.",
    "We are called to be architects of the future, not its victims.",
    "The best way to predict the future is to design it.",
    "There is nothing in a caterpillar that tells you it's going to be a butterfly.",
    "Humanity is acquiring all the right technology for all the wrong reasons.",
    "The minute you choose to do what you really want to do, it's a different kind of life.",
]

class MarkdownRenderer:
    """Simple Markdown renderer for terminal output."""
    
    @staticmethod
    def render(text: str) -> str:
        """Render markdown text with basic formatting."""
        # Headers
        text = re.sub(r'^# (.*?)$', f"\n{Colors.BOLD}{Colors.HEADER}\\1{Colors.ENDC}", text, flags=re.M)
        text = re.sub(r'^## (.*?)$', f"\n{Colors.BOLD}\\1{Colors.ENDC}", text, flags=re.M)
        text = re.sub(r'^### (.*?)$', f"\n{Colors.BOLD}\\1{Colors.ENDC}", text, flags=re.M)
        
        # Bold
        text = re.sub(r'\*\*(.*?)\*\*', f"{Colors.BOLD}\\1{Colors.ENDC}", text)
        
        # Italic
        text = re.sub(r'\*(.*?)\*', f"{Colors.ITALIC}\\1{Colors.ENDC}", text)
        
        # Code blocks
        text = re.sub(r'```(.*?)```', f"{Colors.BLUE}\\1{Colors.ENDC}", text, flags=re.DOTALL)
        
        # Links
        text = re.sub(r'\[(.*?)\]\((.*?)\)', f"{Colors.BLUE}\\1{Colors.ENDC}", text)
        
        return text

class KnowledgeExplorer:
    def __init__(self):
        self.current_path = Path(".")
        self.history = []
        self.markdown_renderer = MarkdownRenderer()
        
    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('clear' if os.name == 'posix' else 'cls')

    def print_header(self):
        """Print the game header."""
        print(f"{Colors.BLUE}{Colors.BOLD}")
        print("""
 ____             _              _           _              _____ _ _           
|  _ \           | |            (_)         | |            |  ___| | |         
| |_) |_   _  ___| | ___ __ ___ _ _ __  ___| |_ ___ _ __ | |_  _| | | ___ _ __ 
|  _ <| | | |/ __| |/ / '_ ` _ \| | '_ \/ __| __/ _ \ '__||  _|| | | |/ _ \ '__|
| |_) | |_| | (__|   <| | | | | | | | | \__ \ ||  __/ |   | | | | | |  __/ |   
|____/ \__,_|\___|_|\_\_| |_| |_|_|_| |_|___/\__\___|_|   \_| |_|_|_|\___|_|   
        """)
        print(f"{Colors.ENDC}")
        print(f"{Colors.GREEN}🌍 Knowledge Graph Explorer 🧠{Colors.ENDC}")
        print(f"{Colors.YELLOW}{random.choice(BUCKY_QUOTES)}{Colors.ENDC}\n")

    def show_loading_animation(self, message: str):
        """Show a loading animation with a message."""
        frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        for _ in range(10):
            for frame in frames:
                sys.stdout.write(f'\r{frame} {message}')
                sys.stdout.flush()
                time.sleep(0.1)
        print("\n")

    def get_directory_contents(self) -> Dict[str, List[str]]:
        """Get contents of current directory."""
        contents = {"dirs": [], "files": [], "markdown_files": []}
        try:
            for item in self.current_path.iterdir():
                if item.is_dir() and not item.name.startswith('.'):
                    contents["dirs"].append(item.name)
                elif item.is_file():
                    if item.suffix.lower() == '.md':
                        contents["markdown_files"].append(item.name)
                    else:
                        contents["files"].append(item.name)
            
            # Sort alphabetically
            contents["dirs"].sort()
            contents["files"].sort()
            contents["markdown_files"].sort()
            
        except Exception as e:
            print(f"{Colors.RED}Error reading directory: {str(e)}{Colors.ENDC}")
        return contents

    def display_menu(self) -> None:
        """Display the main menu."""
        print(f"\n{Colors.BOLD}📍 Current Location:{Colors.ENDC} {self.current_path}")
        print(f"\n{Colors.BOLD}🎯 Available Actions:{Colors.ENDC}")
        print("1. 📂 Browse Repository")
        print("2. 📖 View README")
        print("3. 🔍 Search Files")
        print("4. 💡 Random Bucky Fact")
        print("5. 📜 View File Contents")
        print("6. 🗺️  Show Repository Map")
        print("7. ❌ Exit")
        
    def browse_repository(self) -> None:
        """Browse the repository structure."""
        contents = self.get_directory_contents()
        
        # Show breadcrumb navigation
        parts = self.current_path.parts
        breadcrumb = " > ".join([f"{Colors.BLUE}{p}{Colors.ENDC}" for p in parts])
        print(f"\n📍 {breadcrumb}")
        
        # Show parent directory option if not in root
        if self.current_path != Path("."):
            print(f"\n{Colors.BOLD}⬆️  Parent Directory:{Colors.ENDC}")
            print("0. 📁 ..")
        
        if contents["dirs"]:
            print(f"\n{Colors.BOLD}📂 Directories:{Colors.ENDC}")
            for i, d in enumerate(contents["dirs"], 1):
                print(f"{i}. 📁 {d}")
        
        if contents["markdown_files"]:
            print(f"\n{Colors.BOLD}📝 Markdown Files:{Colors.ENDC}")
            start_idx = len(contents["dirs"]) + 1
            for i, f in enumerate(contents["markdown_files"], start_idx):
                print(f"{i}. 📄 {f}")
        
        if contents["files"]:
            print(f"\n{Colors.BOLD}📄 Other Files:{Colors.ENDC}")
            start_idx = len(contents["dirs"]) + len(contents["markdown_files"]) + 1
            for i, f in enumerate(contents["files"], start_idx):
                print(f"{i}. 📎 {f}")
            
        print(f"\n{Colors.BOLD}Navigation:{Colors.ENDC}")
        print("b. 🔙 Back to Menu")
        
        choice = input("\nEnter your choice: ").lower()
        
        try:
            if choice == "b":
                return
            
            choice_num = int(choice)
            if choice_num == 0 and self.current_path != Path("."):
                self.history.append(self.current_path)
                self.current_path = self.current_path.parent
            elif 1 <= choice_num <= len(contents["dirs"]):
                self.history.append(self.current_path)
                self.current_path = self.current_path / contents["dirs"][choice_num - 1]
            else:
                # Calculate correct file index
                file_idx = choice_num - len(contents["dirs"]) - 1
                if file_idx < len(contents["markdown_files"]):
                    self.view_file(contents["markdown_files"][file_idx], is_markdown=True)
                else:
                    file_idx -= len(contents["markdown_files"])
                    if file_idx < len(contents["files"]):
                        self.view_file(contents["files"][file_idx])
                    
        except (ValueError, IndexError):
            print(f"{Colors.RED}Invalid choice. Please try again.{Colors.ENDC}")
            time.sleep(1)

    def view_file(self, filename: str, is_markdown: bool = False) -> None:
        """View contents of a file."""
        file_path = self.current_path / filename
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            print(f"\n{Colors.BOLD}📄 {filename}{Colors.ENDC}")
            print("=" * 80)
            
            if is_markdown:
                content = self.markdown_renderer.render(content)
            
            # Wrap text for better readability
            wrapped_content = textwrap.fill(content, width=80)
            print(wrapped_content)
            
            print("\nPress Enter to continue...")
            input()
        except Exception as e:
            print(f"{Colors.RED}Error reading file: {str(e)}{Colors.ENDC}")
            time.sleep(2)

    def view_readme(self) -> None:
        """View the README.md file."""
        self.view_file("README.md", is_markdown=True)

    def search_files(self) -> None:
        """Search for files in the repository."""
        search_term = input(f"\n{Colors.BOLD}Enter search term:{Colors.ENDC} ")
        self.show_loading_animation("Searching repository...")
        
        results = []
        try:
            for path in self.current_path.rglob("*"):
                if path.is_file() and search_term.lower() in path.name.lower():
                    results.append(path.relative_to(self.current_path))
        
            if results:
                print(f"\n{Colors.BOLD}🔍 Search Results:{Colors.ENDC}")
                for i, result in enumerate(results, 1):
                    print(f"{i}. 📄 {result}")
                
                choice = input("\nEnter number to view file (or Enter to skip): ")
                if choice.isdigit() and 1 <= int(choice) <= len(results):
                    is_markdown = results[int(choice) - 1].suffix.lower() == '.md'
                    self.view_file(str(results[int(choice) - 1]), is_markdown=is_markdown)
            else:
                print(f"{Colors.YELLOW}No files found matching '{search_term}'{Colors.ENDC}")
                time.sleep(2)
        except Exception as e:
            print(f"{Colors.RED}Error during search: {str(e)}{Colors.ENDC}")
            time.sleep(2)

    def show_repository_map(self) -> None:
        """Display a tree-like map of the repository structure."""
        def print_tree(path: Path, prefix: str = "", is_last: bool = True) -> None:
            print(f"{prefix}{'└── ' if is_last else '├── '}{path.name}")
            prefix += "    " if is_last else "│   "
            
            try:
                paths = sorted(list(path.iterdir()))
                for i, p in enumerate(paths):
                    if not p.name.startswith('.'):
                        print_tree(p, prefix, i == len(paths) - 1)
            except Exception:
                pass
        
        print(f"\n{Colors.BOLD}🗺️  Repository Structure:{Colors.ENDC}\n")
        print_tree(self.current_path)
        input("\nPress Enter to continue...")

    def random_fact(self) -> None:
        """Display a random fact about Buckminster Fuller."""
        facts = [
            "Buckminster Fuller was known as 'Bucky' to his friends and colleagues.",
            "He coined the term 'Spaceship Earth' to describe our planet.",
            "The geodesic dome was one of his most famous inventions.",
            "He was awarded 28 United States patents.",
            "Fuller created the Dymaxion map, a projection of Earth with minimal distortion.",
            "He documented his life in the 'Dymaxion Chronofile', updating it every 15 minutes for over 50 years.",
            "Fuller taught at Black Mountain College, influencing many artists and architects.",
            "He developed the World Game simulation to solve global problems.",
            "The carbon molecule Buckminsterfullerene was named after him.",
            "He wrote more than 30 books, reaching a wide audience with his ideas.",
        ]
        print(f"\n{Colors.BOLD}💡 Did you know?{Colors.ENDC}")
        print(f"{Colors.BLUE}{random.choice(facts)}{Colors.ENDC}")
        input("\nPress Enter to continue...")

    def run(self) -> None:
        """Main game loop."""
        while True:
            try:
                self.clear_screen()
                self.print_header()
                self.display_menu()
                
                choice = input("\nEnter your choice (1-7): ")
                
                if choice == "1":
                    self.browse_repository()
                elif choice == "2":
                    self.view_readme()
                elif choice == "3":
                    self.search_files()
                elif choice == "4":
                    self.random_fact()
                elif choice == "5":
                    filename = input(f"\n{Colors.BOLD}Enter filename to view:{Colors.ENDC} ")
                    is_markdown = filename.lower().endswith('.md')
                    self.view_file(filename, is_markdown=is_markdown)
                elif choice == "6":
                    self.show_repository_map()
                elif choice == "7":
                    self.clear_screen()
                    print(f"{Colors.GREEN}Thank you for exploring the Buckminster Fuller Knowledge Graph!{Colors.ENDC}")
                    print(f"{Colors.YELLOW}Remember: 'The best way to predict the future is to design it.' - Bucky{Colors.ENDC}")
                    sys.exit(0)
                else:
                    print(f"{Colors.RED}Invalid choice. Please enter a number between 1 and 7.{Colors.ENDC}")
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\n\nExiting gracefully...")
                sys.exit(0)
            except Exception as e:
                print(f"{Colors.RED}An error occurred: {str(e)}{Colors.ENDC}")
                print("Press Enter to continue...")
                input()

if __name__ == "__main__":
    try:
        # Ensure we're in the correct directory
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        explorer = KnowledgeExplorer()
        explorer.run()
    except Exception as e:
        print(f"Failed to start: {str(e)}")
        sys.exit(1) 