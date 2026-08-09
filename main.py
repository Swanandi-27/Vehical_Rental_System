from Services.Customer_services import (
    register_customer,
    customer_login
)

from rich.console import Console
from rich.panel import Panel

console = Console()


def main():

    while True:

        console.print(
            Panel(
                """
[bold cyan]1. Customer Register[/bold cyan]
[bold yellow]2. Customer Login[/bold yellow]
[bold red]3. Exit[/bold red]
""",
                title="[bold white]VEHICLE RENTAL SYSTEM[/bold white]",
                border_style="cyan"
            )
        )

        choice = console.input(
            "[bold bright_yellow]Enter Your Choice: [/bold bright_yellow]"
        )

        if choice == "1":

            register_customer()

        elif choice == "2":

            customer_login()

        elif choice == "3":

            console.print(
                "\n[bold green]Thank You for Using Vehicle Rental System![/bold green]"
            )

            console.print(
                "[bold cyan]Visit Again...[/bold cyan]\n"
            )

            break

        else:

            console.print(
                "\n[bold red]Invalid Choice! Please Try Again.[/bold red]\n"
            )


if __name__ == "__main__":
    main()

