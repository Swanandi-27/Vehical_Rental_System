from Services.Customer_services import (
    view_profile,
    update_profile,
    change_password
)

from rich.console import Console
from rich.panel import Panel

console = Console()


def customer_menu(customer_id):

    while True:

        console.print(
            Panel(
                """
[bold cyan]1. View Available Vehicles[/bold cyan]
[bold cyan]2. Search Vehicle[/bold cyan]
[bold cyan]3. Rent Vehicle[/bold cyan]
[bold cyan]4. Return Vehicle[/bold cyan]

[bold yellow]5. Payment[/bold yellow]
[bold yellow]6. View My Rentals[/bold yellow]
[bold yellow]7. Payment History[/bold yellow]

[bold green]8. View My Profile[/bold green]
[bold green]9. Update My Profile[/bold green]
[bold green]10. Change Password[/bold green]

[bold red]11. Logout[/bold red]
""",
                title="[bold white]CUSTOMER MENU[/bold white]",
                border_style="cyan"
            )
        )

        choice = console.input(
            "[bold bright_yellow]Enter Your Choice: [/bold bright_yellow]"
        )

        if choice == "1":

            from Services.Vehicle_services import view_available_vehicle
            view_available_vehicle()

        elif choice == "2":

            from Services.Vehicle_services import search_vehicle
            search_vehicle()

        elif choice == "3":

            from Services.Rental_services import rent_vehicle
            rent_vehicle(customer_id)

        elif choice == "4":

            from Services.Rental_services import return_vehicle
            return_vehicle(customer_id)

        elif choice == "5":

            from Services.Payment_services import payment
            payment(customer_id)

        elif choice == "6":

            from Services.Rental_services import view_my_rentals
            view_my_rentals(customer_id)

        elif choice == "7":

            from Services.Payment_services import payment_history
            payment_history(customer_id)

        elif choice == "8":

            view_profile(customer_id)

        elif choice == "9":

            update_profile(customer_id)

        elif choice == "10":

            change_password(customer_id)

        elif choice == "11":

            console.print(
                "\n[bold green]Customer Logout Successfully![/bold green]\n"
            )
            break

        else:

            console.print(
                "\n[bold red]Invalid Choice! Please Try Again.[/bold red]\n"
            )

