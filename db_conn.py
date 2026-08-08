import mysql.connector
from rich.console import Console

console = Console()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="vehicle_rental_system"
)

cursor = conn.cursor()

console.print(
    "[bold green]✓ Database Connected Successfully![/bold green]"
)

