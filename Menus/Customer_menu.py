from Services.Customer_services import *
from Services.vehicle_services import *
from Services.rental_services import *

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
[bold yellow]5. View My Rentals[/bold yellow]
[bold yellow]6. Payment History[/bold yellow]

[bold green]7. View My Profile[/bold green]
[bold green]8. Update My Profile[/bold green]
[bold green]9. Change Password[/bold green]

[bold red]10. Logout[/bold red]
""",
                title="[bold white]CUSTOMER MENU[/bold white]",
                border_style="cyan"
            )
        )

        choice = console.input(
            "[bold bright_yellow]Enter Your Choice: [/bold bright_yellow]"
        )

        if choice == "1":

            
            view_available_vehicle()

        elif choice == "2":
            Search_vehicle()

            pass

        elif choice == "3":

            
            rent_vehicle(customer_id)
            

        elif choice == "4":

            
            return_vehicle(customer_id)
           
        

        elif choice == "5":

            
            view_my_rentals(customer_id)
           

        elif choice == "6":

            
            payment_history(customer_id)

        elif choice == "7":

            view_profile(customer_id)

        elif choice == "8":

            update_profile(customer_id)

        elif choice == "9":

            change_password(customer_id)

        elif choice == "10":

            console.print(
                "\n[bold green]Customer Logout Successfully![/bold green]\n"
            )
            break

        else:

            console.print(
                "\n[bold red]Invalid Choice! Please Try Again.[/bold red]\n"
            )

