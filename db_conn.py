import mysql.connector
from rich.console import Console

console = Console()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="swanandi",
    database="python45"
)

cursor = conn.cursor()

console.print(
    "[bold green]✓ Database Connected Successfully![/bold green]"
)

