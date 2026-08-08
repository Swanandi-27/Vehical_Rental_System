from rich.console import Console
from rich.table import Table

console = Console()


class Customer:

    def __init__(
        self,
        customer_id,
        customer_name,
        username,
        phone,
        email,
        password,
        license_no,
        address
    ):

        self.customer_id = customer_id
        self.customer_name = customer_name
        self.username = username
        self.phone = phone
        self.email = email
        self.password = password
        self.license_no = license_no
        self.address = address

    def get_data(self):

        return (
            self.customer_name,
            self.username,
            self.phone,
            self.email,
            self.password,
            self.license_no,
            self.address
        )

    def display_customer(self):

        table = Table(
            title="[bold cyan]CUSTOMER DETAILS[/bold cyan]",
            border_style="cyan",
            show_lines=True
        )

        table.add_column(
            "Customer ID",
            style="bold cyan"
        )

        table.add_column(
            "Customer Name",
            style="bold yellow"
        )

        table.add_column(
            "Username",
            style="bold green"
        )

        table.add_column(
            "Phone",
            style="bold magenta"
        )

        table.add_column(
            "Email",
            style="bold blue"
        )

        table.add_column(
            "Password",
            style="bold red"
        )

        table.add_column(
            "License No",
            style="bold bright_cyan"
        )

        table.add_column(
            "Address",
            style="bold bright_green"
        )

        table.add_row(
            str(self.customer_id),
            str(self.customer_name),
            str(self.username),
            str(self.phone),
            str(self.email),
            str(self.password),
            str(self.license_no),
            str(self.address)
        )

        console.print(table)

