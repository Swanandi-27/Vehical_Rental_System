from db_conn import conn, cursor
from Models.Customer import Customer

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

#customer res

def register_customer():

    console.print(
        Panel(
            "[bold cyan]CUSTOMER REGISTER[/bold cyan]",
            border_style="cyan"
        )
    )

    name = console.input(
        "[bold yellow]Enter Customer Name : [/bold yellow]"
    )

    username = console.input(
        "[bold yellow]Enter Username      : [/bold yellow]"
    )

    phone = console.input(
        "[bold yellow]Enter Phone Number  : [/bold yellow]"
    )

    email = console.input(
        "[bold yellow]Enter Email         : [/bold yellow]"
    )

    password = console.input(
        "[bold yellow]Enter Password      : [/bold yellow]"
    )

    license_no = console.input(
        "[bold yellow]Enter License No    : [/bold yellow]"
    )

    address = console.input(
        "[bold yellow]Enter Address       : [/bold yellow]"
    )

    customer = Customer(
        None,
        name,
        username,
        phone,
        email,
        password,
        license_no,
        address
    )

    cursor.execute("""
        INSERT INTO customer
        (customer_name, username, phone, email, password, license_no, address)
        VALUES(%s,%s,%s,%s,%s,%s,%s)
    """, customer.get_data())

    conn.commit()

    console.print(
        Panel(
            "[bold green]✓ Customer Registered Successfully![/bold green]",
            border_style="green"
        )
    )


#customer login

def customer_login():

    console.print(
        Panel(
            "[bold cyan]CUSTOMER LOGIN[/bold cyan]",
            border_style="cyan"
        )
    )

    username = console.input(
        "[bold yellow]Enter Username : [/bold yellow]"
    )

    password = console.input(
        "[bold yellow]Enter Password : [/bold yellow]"
    )

    cursor.execute("""
        SELECT customer_id
        FROM customer
        WHERE username=%s AND password=%s
    """, (username, password))

    customer = cursor.fetchone()

    if customer:

        console.print(
            Panel(
                "[bold green]✓ Login Successful![/bold green]",
                border_style="green"
            )
        )

        from Menus.Customer_menu import customer_menu
        customer_menu(customer[0])

    else:

        console.print(
            Panel(
                "[bold red]✗ Invalid Username or Password.[/bold red]",
                border_style="red"
            )
        )


#view customer

def view_customers():

    cursor.execute("SELECT * FROM customer")

    data = cursor.fetchall()

    if not data:

        console.print(
            "[bold red]✗ No Customers Found.[/bold red]"
        )
        return

    console.print(
        Panel(
            "[bold cyan]CUSTOMER LIST[/bold cyan]",
            border_style="cyan"
        )
    )

    table = Table(
        title="[bold cyan]CUSTOMERS[/bold cyan]",
        border_style="cyan",
        show_lines=True
    )

    table.add_column("ID", style="bold cyan")
    table.add_column("Name", style="bold yellow")
    table.add_column("Username", style="bold green")
    table.add_column("Phone", style="bold magenta")
    table.add_column("Email", style="bold blue")
    table.add_column("Password", style="bold red")
    table.add_column("License No", style="bold bright_cyan")
    table.add_column("Address", style="bold bright_green")

    for c in data:

        table.add_row(
            str(c[0]),
            str(c[1]),
            str(c[2]),
            str(c[3]),
            str(c[4]),
            str(c[5]),
            str(c[6]),
            str(c[7])
        )

    console.print(table)


#search customer

def search_customer():

    while True:

        console.print(
            Panel(
                """
[bold cyan]1. Search By ID[/bold cyan]
[bold yellow]2. Search By Name[/bold yellow]
[bold green]3. Search By Phone[/bold green]
[bold magenta]4. Search By Email[/bold magenta]
[bold red]5. Back[/bold red]
""",
                title="[bold white]SEARCH CUSTOMER[/bold white]",
                border_style="cyan"
            )
        )

        choice = console.input(
            "[bold bright_yellow]Enter Choice : [/bold bright_yellow]"
        )

        if choice == "1":

            cid = int(
                console.input(
                    "[bold yellow]Enter Customer ID : [/bold yellow]"
                )
            )

            cursor.execute(
                "SELECT * FROM customer WHERE customer_id=%s",
                (cid,)
            )

        elif choice == "2":

            name = console.input(
                "[bold yellow]Enter Name : [/bold yellow]"
            )

            cursor.execute(
                "SELECT * FROM customer WHERE customer_name=%s",
                (name,)
            )

        elif choice == "3":

            phone = console.input(
                "[bold yellow]Enter Phone : [/bold yellow]"
            )

            cursor.execute(
                "SELECT * FROM customer WHERE phone=%s",
                (phone,)
            )

        elif choice == "4":

            email = console.input(
                "[bold yellow]Enter Email : [/bold yellow]"
            )

            cursor.execute(
                "SELECT * FROM customer WHERE email=%s",
                (email,)
            )

        elif choice == "5":

            break

        else:

            console.print(
                "[bold red]✗ Invalid Choice.[/bold red]"
            )

            continue

        customers = cursor.fetchall()

        if customers:

            table = Table(
                title="[bold cyan]SEARCH RESULT[/bold cyan]",
                border_style="cyan",
                show_lines=True
            )

            table.add_column("ID", style="bold cyan")
            table.add_column("Name", style="bold yellow")
            table.add_column("Username", style="bold green")
            table.add_column("Phone", style="bold magenta")
            table.add_column("Email", style="bold blue")
            table.add_column("Password", style="bold red")
            table.add_column("License No", style="bold bright_cyan")
            table.add_column("Address", style="bold bright_green")

            for c in customers:

                table.add_row(
                    str(c[0]),
                    str(c[1]),
                    str(c[2]),
                    str(c[3]),
                    str(c[4]),
                    str(c[5]),
                    str(c[6]),
                    str(c[7])
                )

            console.print(table)

        else:

            console.print(
                "\n[bold red]✗ Customer Not Found.[/bold red]\n"
            )


#update customer

def update_customer():

    cid = int(
        console.input(
            "[bold yellow]Enter Customer ID : [/bold yellow]"
        )
    )

    cursor.execute(
        "SELECT * FROM customer WHERE customer_id=%s",
        (cid,)
    )

    data = cursor.fetchone()

    if not data:

        console.print(
            "\n[bold red]✗ Customer Not Found.[/bold red]\n"
        )
        return

    while True:

        console.print(
            Panel(
                """
[bold cyan]1. Update All Details[/bold cyan]
[bold yellow]2. Update Name[/bold yellow]
[bold green]3. Update Phone[/bold green]
[bold blue]4. Update Email[/bold blue]
[bold magenta]5. Update License No[/bold magenta]
[bold bright_cyan]6. Update Address[/bold bright_cyan]
[bold red]7. Back[/bold red]
""",
                title="[bold white]UPDATE CUSTOMER[/bold white]",
                border_style="cyan"
            )
        )

        choice = console.input(
            "[bold bright_yellow]Enter Choice : [/bold bright_yellow]"
        )

        if choice == "1":

            name = console.input(
                "[bold yellow]Enter Name : [/bold yellow]"
            )

            phone = console.input(
                "[bold yellow]Enter Phone : [/bold yellow]"
            )

            email = console.input(
                "[bold yellow]Enter Email : [/bold yellow]"
            )

            license_no = console.input(
                "[bold yellow]Enter License No : [/bold yellow]"
            )

            address = console.input(
                "[bold yellow]Enter Address : [/bold yellow]"
            )

            cursor.execute("""
                UPDATE customer
                SET customer_name=%s,
                    phone=%s,
                    email=%s,
                    license_no=%s,
                    address=%s
                WHERE customer_id=%s
            """, (name, phone, email, license_no, address, cid))

            conn.commit()

            console.print(
                "[bold green]✓ Customer Updated Successfully![/bold green]"
            )

        elif choice == "2":

            name = console.input(
                "[bold yellow]Enter New Name : [/bold yellow]"
            )

            cursor.execute("""
                UPDATE customer
                SET customer_name=%s
                WHERE customer_id=%s
            """, (name, cid))

            conn.commit()

            console.print(
                "[bold green]✓ Name Updated Successfully![/bold green]"
            )

        elif choice == "3":

            phone = console.input(
                "[bold yellow]Enter New Phone : [/bold yellow]"
            )

            cursor.execute("""
                UPDATE customer
                SET phone=%s
                WHERE customer_id=%s
            """, (phone, cid))

            conn.commit()

            console.print(
                "[bold green]✓ Phone Updated Successfully![/bold green]"
            )

        elif choice == "4":

            email = console.input(
                "[bold yellow]Enter New Email : [/bold yellow]"
            )

            cursor.execute("""
                UPDATE customer
                SET email=%s
                WHERE customer_id=%s
            """, (email, cid))

            conn.commit()

            console.print(
                "[bold green]✓ Email Updated Successfully![/bold green]"
            )

        elif choice == "5":

            license_no = console.input(
                "[bold yellow]Enter New License No : [/bold yellow]"
            )

            cursor.execute("""
                UPDATE customer
                SET license_no=%s
                WHERE customer_id=%s
            """, (license_no, cid))

            conn.commit()

            console.print(
                "[bold green]✓ License Updated Successfully![/bold green]"
            )

        elif choice == "6":

            address = console.input(
                "[bold yellow]Enter New Address : [/bold yellow]"
            )

            cursor.execute("""
                UPDATE customer
                SET address=%s
                WHERE customer_id=%s
            """, (address, cid))

            conn.commit()

            console.print(
                "[bold green]✓ Address Updated Successfully![/bold green]"
            )

        elif choice == "7":

            break

        else:

            console.print(
                "[bold red]✗ Invalid Choice![/bold red]"
            )

#delete customer

def delete_customer():

    cid = int(
        console.input(
            "[bold yellow]Enter Customer ID : [/bold yellow]"
        )
    )

    cursor.execute(
        "SELECT * FROM customer WHERE customer_id=%s",
        (cid,)
    )

    data = cursor.fetchone()

    if not data:

        console.print(
            "\n[bold red]✗ Customer Not Found.[/bold red]\n"
        )
        return

    confirm = console.input(
        "[bold bright_yellow]Are you sure you want to delete this customer? (Y/N): [/bold bright_yellow]"
    )

    if confirm.lower() == "y":

        cursor.execute(
            "DELETE FROM customer WHERE customer_id=%s",
            (cid,)
        )

        conn.commit()

        console.print(
            Panel(
                "[bold green]✓ Customer Deleted Successfully![/bold green]",
                border_style="green"
            )
        )

    else:

        console.print(
            "[bold yellow]Delete Cancelled.[/bold yellow]"
        )

#view profile

def view_profile(customer_id):

    cursor.execute("""
        SELECT *
        FROM customer
        WHERE customer_id=%s
    """, (customer_id,))

    data = cursor.fetchone()

    if data:

        table = Table(
            title="[bold cyan]MY PROFILE[/bold cyan]",
            border_style="cyan",
            show_lines=True
        )

        table.add_column("Field", style="bold yellow")
        table.add_column("Details", style="bold green")

        table.add_row("Customer ID", str(data[0]))
        table.add_row("Customer Name", str(data[1]))
        table.add_row("Username", str(data[2]))
        table.add_row("Phone", str(data[3]))
        table.add_row("Email", str(data[4]))
        table.add_row("Password", str(data[5]))
        table.add_row("License No", str(data[6]))
        table.add_row("Address", str(data[7]))

        console.print(table)

    else:

        console.print(
            "\n[bold red]✗ Profile Not Found.[/bold red]\n"
        )

#update profile

def update_profile(customer_id):

    while True:

        console.print(
            Panel(
                """
[bold cyan]1. Update Name[/bold cyan]
[bold yellow]2. Update Phone[/bold yellow]
[bold green]3. Update Email[/bold green]
[bold blue]4. Update License No[/bold blue]
[bold magenta]5. Update Address[/bold magenta]
[bold red]6. Back[/bold red]
""",
                title="[bold white]UPDATE MY PROFILE[/bold white]",
                border_style="cyan"
            )
        )

        choice = console.input(
            "[bold bright_yellow]Enter Choice : [/bold bright_yellow]"
        )

        if choice == "1":

            name = console.input(
                "[bold yellow]Enter New Name : [/bold yellow]"
            )

            cursor.execute("""
                UPDATE customer
                SET customer_name=%s
                WHERE customer_id=%s
            """, (name, customer_id))

            conn.commit()

            console.print(
                "[bold green]✓ Name Updated Successfully![/bold green]"
            )

        elif choice == "2":

            phone = console.input(
                "[bold yellow]Enter New Phone : [/bold yellow]"
            )

            cursor.execute("""
                UPDATE customer
                SET phone=%s
                WHERE customer_id=%s
            """, (phone, customer_id))

            conn.commit()

            console.print(
                "[bold green]✓ Phone Updated Successfully![/bold green]"
            )

        elif choice == "3":

            email = console.input(
                "[bold yellow]Enter New Email : [/bold yellow]"
            )

            cursor.execute("""
                UPDATE customer
                SET email=%s
                WHERE customer_id=%s
            """, (email, customer_id))

            conn.commit()

            console.print(
                "[bold green]✓ Email Updated Successfully![/bold green]"
            )

        elif choice == "4":

            license_no = console.input(
                "[bold yellow]Enter New License No : [/bold yellow]"
            )

            cursor.execute("""
                UPDATE customer
                SET license_no=%s
                WHERE customer_id=%s
            """, (license_no, customer_id))

            conn.commit()

            console.print(
                "[bold green]✓ License Number Updated Successfully![/bold green]"
            )

        elif choice == "5":

            address = console.input(
                "[bold yellow]Enter New Address : [/bold yellow]"
            )

            cursor.execute("""
                UPDATE customer
                SET address=%s
                WHERE customer_id=%s
            """, (address, customer_id))

            conn.commit()

            console.print(
                "[bold green]✓ Address Updated Successfully![/bold green]"
            )

        elif choice == "6":

            break

        else:

            console.print(
                "[bold red]✗ Invalid Choice![/bold red]"
            )

#change pass

def change_password(customer_id):

    cursor.execute(
        "SELECT password FROM customer WHERE customer_id=%s",
        (customer_id,)
    )

    data = cursor.fetchone()

    if not data:

        console.print(
            "\n[bold red]✗ Customer Not Found.[/bold red]\n"
        )
        return

    current_password = console.input(
        "[bold yellow]Enter Current Password : [/bold yellow]"
    )

    if current_password != data[0]:

        console.print(
            "\n[bold red]✗ Current Password is Incorrect.[/bold red]\n"
        )
        return

    new_password = console.input(
        "[bold yellow]Enter New Password : [/bold yellow]"
    )

    confirm_password = console.input(
        "[bold yellow]Confirm New Password : [/bold yellow]"
    )

    if new_password != confirm_password:

        console.print(
            "\n[bold red]✗ Passwords do not match.[/bold red]\n"
        )
        return

    cursor.execute("""
        UPDATE customer
        SET password=%s
        WHERE customer_id=%s
    """, (new_password, customer_id))

    conn.commit()

    console.print(
        Panel(
            "[bold green]✓ Password Changed Successfully![/bold green]",
            border_style="green"
        )
    )

