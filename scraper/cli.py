import os
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

# Import YOUR custom modules from the files we just made
from .engine import fetch_and_parse
from .cleaner import clean_ml_features

console = Console()

def main():
    console.print(Panel.fit("[bold cyan]Universal Web Table Scraper[/bold cyan]", border_style="cyan"))
    target_url = Prompt.ask("[bold yellow]Enter the target URL[/bold yellow]")
    
    # --- NEW: Dynamic Desktop Routing ---
    # os.path.expanduser("~") automatically grabs the current user's Home folder (e.g., C:\Users\mathu)
    user_home = os.path.expanduser("~")
    output_folder = os.path.join(user_home, "Desktop", "csv_files")
        
    os.makedirs(output_folder, exist_ok=True)
        
    # Tell the user exactly where the files are going so they aren't confused
    console.print(f"[dim]Routing outputs to: {output_folder}[/dim]\n")

    with console.status("[bold cyan]Fetching webpage...", spinner="dots"):
        tables, safe_title, status = fetch_and_parse(target_url)

    if status != 200:
        console.print(f"[bold red]✖ Failed with status: {status}[/bold red]")
        # LEVEL 1 PAUSE: Keeps window open if double-clicked
        input("\nPress Enter to exit...") 
        return

    if not tables:
        console.print("[bold yellow]No tables found.[/bold yellow]")
        input("\nPress Enter to exit...")
        return

    valid_count = 0
    with console.status("[bold magenta]Cleaning data...", spinner="line"):
        for df in tables:
            if df.empty or len(df) < 1: continue
            
            df = clean_ml_features(df)
            valid_count += 1
            filename = f"{safe_title}_table_{valid_count}.csv"
            df.to_csv(os.path.join(output_folder, filename), index=False)
            console.print(f"[bold blue]↳ Saved:[/bold blue] {filename}")

    console.print(f"\n[bold green]✔ Extracted {valid_count} tables.[/bold green]")
    input("\nPress Enter to exit...") # LEVEL 1 PAUSE

# This tells Python to run main() if this file is executed directly
if __name__ == "__main__":
    main()