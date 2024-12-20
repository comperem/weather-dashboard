from rich import print as rprint
from .utils import print_collection_stats


def check_analysis_results(db):
    """Check contents of analysis collections"""
    rprint(f"\n[bold blue]{'='*60}[/bold blue]")
    rprint("[bold green]Analysis Collections Status[/bold green]")
    rprint(f"[bold blue]{'='*60}[/bold blue]\n")

    for collection_name in ["weather_data", "eda_results", "pca_results", "ml_results"]:
        print_collection_stats(db[collection_name], collection_name)
