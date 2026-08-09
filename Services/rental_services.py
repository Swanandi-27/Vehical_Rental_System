from db_conn import conn,cursor
from Models.rental import rental
from Models.payment import Payment
from datetime import date
from Services.payment_services import *




from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from datetime import datetime

console = Console()
 
 
#---------------- RENT VEHICLE ---------------- #
 

 




def rent_vehicle(customer_id):

    console.print(
        Panel.fit(
            "[bold cyan]RENT VEHICLE[/bold cyan]",
            border_style="cyan"
        )
    )

    vehicle_id = int(input("Enter Vehicle ID: "))

    rent_date = input("Enter Rent Date (YYYY-MM-DD): ")
    return_date = input("Enter Return Date (YYYY-MM-DD): ")

    # Convert string to date
    rent_date_obj = date.fromisoformat(rent_date)
    return_date_obj = date.fromisoformat(return_date)

    # Calculate total days
    total_days = (return_date_obj - rent_date_obj).days

    console.print(f"Total Days : {total_days}")

    if total_days <= 0:
        console.print(
            "❌ Number of days must be greater than 0.",
            style="bold red"
        )
        return

    # Check vehicle availability
    query = """
        SELECT rent_per_day
        FROM vehicle
        WHERE vehicle_id = %s
        AND status = 'Available'
    """

    cursor.execute(query, (vehicle_id,))
    vehicle = cursor.fetchone()

    if vehicle is None:
        console.print(
            "❌ Vehicle is not available!",
            style="bold red"
        )
        return

    rent_per_day = float(vehicle[0])

    # Calculate total amount
    total_amount = rent_per_day * total_days

    console.print(
        f"\nTotal Amount to Pay : ₹{total_amount}",
        style="bold yellow"
    )

    # Payment method
    payment_method = input(
        "Enter Payment Method (Cash/UPI/Card): "
    )

    # Validate payment method
    payment_method = payment_method.capitalize()

    if payment_method not in ["Cash", "Upi", "Card"]:
        console.print(
            "❌ Invalid payment method!",
            style="bold red"
        )
        return

    if payment_method == "Upi":
        payment_method = "UPI"

    try:

        # -----------------------------
        # CREATE RENTAL
        # -----------------------------

        rental1 = rental(
            customer_id,
            vehicle_id,
            rent_date,
            return_date,
            total_days,
            total_amount,
            "Active"
        )

        rental_query = """
            INSERT INTO rental
            (
                customer_id,
                vehicle_id,
                rent_date,
                return_date,
                total_days,
                total_amount,
                rental_status
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s)
        """

        rental_values = (
            rental1.customer_id,
            rental1.vehicle_id,
            rental1.rent_date,
            rental1.return_date,
            rental1.total_days,
            rental1.total_amount,
            rental1.rental_status
        )

        cursor.execute(rental_query, rental_values)

        # Get generated Rental ID
        rental_id = cursor.lastrowid

        # -----------------------------
        # MAKE PAYMENT
        # -----------------------------

        payment_success = make_payment(
            rental_id,
            payment_method,
            "Paid"
        )

        if not payment_success:
            conn.rollback()

            console.print(
                "❌ Payment failed. Rental cancelled.",
                style="bold red"
            )
            return

        # -----------------------------
        # UPDATE VEHICLE STATUS
        # -----------------------------

        update_query = """
            UPDATE vehicle
            SET status = 'Rented'
            WHERE vehicle_id = %s
        """

        cursor.execute(update_query, (vehicle_id,))

        # Commit everything
        conn.commit()

        # -----------------------------
        # RECEIPT
        # -----------------------------

        console.print(
            Panel.fit(
                f"""
[bold green]Vehicle Rented Successfully![/bold green]

Rental ID      : {rental_id}
Vehicle ID     : {vehicle_id}
Rent Date      : {rent_date}
Return Date    : {return_date}
Total Days     : {total_days}
Amount Paid    : ₹{total_amount}
Payment Method : {payment_method}
Payment Status : Paid
""",
                title="Rental Receipt",
                border_style="green"
            )
        )

    except Exception as e:

        conn.rollback()

        console.print(
            f"❌ Rental failed: {e}",
            style="bold red"
        )
 
#---------------- VIEW MY RENTALS ---------------- #
 
def view_my_rentals(customer_id):
 
    query = """
    SELECT
        r.rental_id,
        v.brand,
        v.model,
        r.rent_date,
        r.return_date,
        r.total_days,
        r.total_amount,
        r.rental_status
    FROM rental r
    JOIN vehicle v
    ON r.vehicle_id = v.vehicle_id
    WHERE r.customer_id=%s
    """
 
    cursor.execute(query, (customer_id,))
    rentals = cursor.fetchall() 
    if not rentals:
        console.print("❌ No Rental Records Found!", style="bold red")
        return 
    table = Table(title="My Rentals")
 
    table.add_column("Rental ID")
    table.add_column("Brand")
    table.add_column("Model")
    table.add_column("Rent Date")
    table.add_column("Return Date")
    table.add_column("Days")
    table.add_column("Amount")
    table.add_column("Status")

    for r in rentals:
 
        table.add_row(
            str(r[0]),
            r[1],
            r[2],
            str(r[3]),
            str(r[4]),
            str(r[5]),
            str(r[6]),
            r[7]
        )
 
    console.print(table)

#---------------------View All Rentals-------------------- #admin
def view_all_rental():

    query = """
    SELECT
        r.rental_id,
        c.customer_name,
        v.brand,
        v.model,
        r.rent_date,
        r.return_date,
        r.total_days,
        r.total_amount,
        r.rental_status
    FROM rental r
    JOIN customer c
        ON r.customer_id = c.customer_id
    JOIN vehicle v
        ON r.vehicle_id = v.vehicle_id
    """

    cursor.execute(query)

    rentals = cursor.fetchall()

    if not rentals:
        console.print("❌ No Rental Records Found!", style="bold red")
        return

    table = Table(title="All Rentals")

    table.add_column("Rental ID", style="cyan")
    table.add_column("Customer", style="green")
    table.add_column("Brand")
    table.add_column("Model")
    table.add_column("Rent Date")
    table.add_column("Return Date")
    table.add_column("Days")
    table.add_column("Amount")
    table.add_column("Status")

    for r in rentals:

        table.add_row(
            str(r[0]),
            r[1],
            r[2],
            r[3],
            str(r[4]),
            str(r[5]),
            str(r[6]),
            f"₹{r[7]}",
            r[8]
        )

    console.print(table)



 
 
 
#---------------- RETURN VEHICLE ---------------- #
 
def return_vehicle(customer_id):
   
 
   rental_id = int(input("Enter Rental ID: "))
   query = """
   SELECT vehicle_id
   FROM rental
   WHERE rental_id=%s
   AND customer_id=%s
   AND rental_status='Active'
   """
   cursor.execute(query, (rental_id, customer_id))
   rental = cursor.fetchone()
   if rental is None:
    console.print("❌ Rental Record Not Found!", style="bold red")
    return
   vehicle_id = rental[0]
   today = datetime.today().strftime("%Y-%m-%d")
   cursor.execute("""
   UPDATE rental
   SET return_date=%s,
      rental_status='Completed'
    WHERE rental_id=%s
    """, (today, rental_id))
   cursor.execute("""
   UPDATE vehicle
   SET status='Available'
   WHERE vehicle_id=%s
   """, (vehicle_id,))
   conn.commit()
   console.print("✅ Vehicle Returned Successfully!", style="bold green")



#-------------------------------Search Rental------------------------ #admin
def search_rental():

    while True:

        console.print(
            Panel.fit(
                "[bold cyan]Search Rental[/bold cyan]"
            )
        )

        console.print(
            "\n1. Search by Rental ID"
            "\n2. Search By Customer Name"
            "\n3. Search by Vehicle Registration No"
            "\n4. Search by Rental Status"
            "\n5. Back"
        )

        ch = int(input("Enter your choice: "))

        match ch:

            # ---------------------------------
            # SEARCH BY RENTAL ID
            # ---------------------------------

            case 1:

                rental_id = int(
                    input("Enter Rental ID: ")
                )

                query = """
                    SELECT
                        r.rental_id,
                        c.customer_name,
                        v.brand,
                        v.model,
                        v.registration_no,
                        r.rent_date,
                        r.return_date,
                        r.total_days,
                        r.total_amount,
                        r.rental_status
                    FROM rental r
                    JOIN customer c
                        ON r.customer_id = c.customer_id
                    JOIN vehicle v
                        ON r.vehicle_id = v.vehicle_id
                    WHERE r.rental_id = %s
                """

                cursor.execute(
                    query,
                    (rental_id,)
                )

                rentals = cursor.fetchall()

            # ---------------------------------
            # SEARCH BY CUSTOMER NAME
            # ---------------------------------

            case 2:

                name = input(
                    "Enter Customer Name: "
                )

                query = """
                    SELECT
                        r.rental_id,
                        c.customer_name,
                        v.brand,
                        v.model,
                        v.registration_no,
                        r.rent_date,
                        r.return_date,
                        r.total_days,
                        r.total_amount,
                        r.rental_status
                    FROM rental r
                    JOIN customer c
                        ON r.customer_id = c.customer_id
                    JOIN vehicle v
                        ON r.vehicle_id = v.vehicle_id
                    WHERE c.customer_name = %s
                """

                cursor.execute(
                    query,
                    (name,)
                )

                rentals = cursor.fetchall()

            # ---------------------------------
            # SEARCH BY REGISTRATION NUMBER
            # ---------------------------------

            case 3:

                registration_no = input(
                    "Enter Registration No: "
                )

                query = """
                    SELECT
                        r.rental_id,
                        c.customer_name,
                        v.brand,
                        v.model,
                        v.registration_no,
                        r.rent_date,
                        r.return_date,
                        r.total_days,
                        r.total_amount,
                        r.rental_status
                    FROM rental r
                    JOIN customer c
                        ON r.customer_id = c.customer_id
                    JOIN vehicle v
                        ON r.vehicle_id = v.vehicle_id
                    WHERE v.registration_no = %s
                """

                cursor.execute(
                    query,
                    (registration_no,)
                )

                rentals = cursor.fetchall()

            # ---------------------------------
            # SEARCH BY STATUS
            # ---------------------------------

            case 4:

                status = input(
                    "Enter Status (Active/Completed): "
                ).strip().capitalize()

                query = """
                    SELECT
                        r.rental_id,
                        c.customer_name,
                        v.brand,
                        v.model,
                        v.registration_no,
                        r.rent_date,
                        r.return_date,
                        r.total_days,
                        r.total_amount,
                        r.rental_status
                    FROM rental r
                    JOIN customer c
                        ON r.customer_id = c.customer_id
                    JOIN vehicle v
                        ON r.vehicle_id = v.vehicle_id
                    WHERE r.rental_status = %s
                """

                cursor.execute(
                    query,
                    (status,)
                )

                rentals = cursor.fetchall()

            # ---------------------------------
            # BACK
            # ---------------------------------

            case 5:

                break

            case _:

                console.print(
                    "❌ Invalid Choice!",
                    style="bold red"
                )

                continue

        # ---------------------------------
        # DISPLAY RESULT
        # ---------------------------------

        if not rentals:

            console.print(
                "❌ No Rental Records Found!",
                style="bold red"
            )

            continue

        table = Table(
            title="Rental Details"
        )

        table.add_column(
            "Rental ID",
            style="cyan"
        )

        table.add_column(
            "Customer",
            style="green"
        )

        table.add_column("Brand")
        table.add_column("Model")
        table.add_column("Registration No")
        table.add_column("Rent Date")
        table.add_column("Return Date")
        table.add_column("Days")
        table.add_column("Amount")
        table.add_column("Status")

        for r in rentals:

            table.add_row(
                str(r[0]),
                r[1],
                r[2],
                r[3],
                r[4],
                str(r[5]),
                str(r[6]),
                str(r[7]),
                str(r[8]),
                r[9]
            )

        console.print(table)

def update_rental():

    rental_id = int(input("Enter Rental ID: "))

    cursor.execute(
        """
        SELECT *
        FROM rental
        WHERE rental_id = %s
        """,
        (rental_id,)
    )

    rental = cursor.fetchone()

    if not rental:

        console.print(
            "❌ Rental Not Found!",
            style="bold red"
        )

        return

    while True:

        console.print(
            "\n[bold cyan]===== UPDATE RENTAL =====[/bold cyan]"
        )

        console.print(
            """
1. Update Rent Date
2. Update Return Date
3. Update Total Amount
4. Update Rental Status
5. Update All Details
6. Back
"""
        )

        choice = input("Enter Your Choice: ")

        # --------------------------------
        # UPDATE RENT DATE
        # --------------------------------

        if choice == "1":

            new_rent_date = input(
                "Enter New Rent Date (YYYY-MM-DD): "
            )

            new_rent_date = date.fromisoformat(
                new_rent_date
            )

            cursor.execute(
                """
                UPDATE rental
                SET rent_date = %s
                WHERE rental_id = %s
                """,
                (new_rent_date, rental_id)
            )

            conn.commit()

            console.print(
                "✅ Rent Date Updated Successfully!",
                style="bold green"
            )

            show_rental(rental_id)

        # --------------------------------
        # UPDATE RETURN DATE
        # --------------------------------

        elif choice == "2":

            new_return_date = input(
                "Enter New Return Date (YYYY-MM-DD): "
            )

            new_return_date = date.fromisoformat(
                new_return_date
            )

            cursor.execute(
                """
                SELECT rent_date
                FROM rental
                WHERE rental_id = %s
                """,
                (rental_id,)
            )

            rent_date = cursor.fetchone()[0]

            if new_return_date < rent_date:

                console.print(
                    "❌ Return date cannot be before rent date!",
                    style="bold red"
                )

                continue

            total_days = (
                new_return_date - rent_date
            ).days

            if total_days == 0:
                total_days = 1

            cursor.execute(
                """
                SELECT v.rent_per_day
                FROM rental r
                JOIN vehicle v
                ON r.vehicle_id = v.vehicle_id
                WHERE r.rental_id = %s
                """,
                (rental_id,)
            )

            rent_per_day = cursor.fetchone()[0]

            total_amount = total_days * rent_per_day

            cursor.execute(
                """
                UPDATE rental
                SET return_date = %s,
                    total_days = %s,
                    total_amount = %s
                WHERE rental_id = %s
                """,
                (
                    new_return_date,
                    total_days,
                    total_amount,
                    rental_id
                )
            )

            conn.commit()

            console.print(
                "✅ Return Date Updated Successfully!",
                style="bold green"
            )

            show_rental(rental_id)

        # --------------------------------
        # UPDATE TOTAL AMOUNT
        # --------------------------------

        elif choice == "3":

            new_amount = float(
                input("Enter New Total Amount: ")
            )

            cursor.execute(
                """
                UPDATE rental
                SET total_amount = %s
                WHERE rental_id = %s
                """,
                (new_amount, rental_id)
            )

            conn.commit()

            console.print(
                "✅ Total Amount Updated Successfully!",
                style="bold green"
            )

            show_rental(rental_id)

        # --------------------------------
        # UPDATE STATUS
        # --------------------------------

        elif choice == "4":

            console.print(
                "\n[bold yellow]1. Active[/bold yellow]"
            )

            console.print(
                "[bold green]2. Completed[/bold green]"
            )

            status_choice = input(
                "Enter Status: "
            )

            if status_choice == "1":
                new_status = "Active"

            elif status_choice == "2":
                new_status = "Completed"

            else:
                console.print(
                    "❌ Invalid Status!",
                    style="bold red"
                )
                continue

            cursor.execute(
                """
                UPDATE rental
                SET rental_status = %s
                WHERE rental_id = %s
                """,
                (new_status, rental_id)
            )

            conn.commit()

            console.print(
                "✅ Rental Status Updated Successfully!",
                style="bold green"
            )

            show_rental(rental_id)

        # --------------------------------
        # UPDATE ALL DETAILS
        # --------------------------------

        elif choice == "5":

            new_rent_date = date.fromisoformat(
                input("Enter Rent Date (YYYY-MM-DD): ")
            )

            new_return_date = date.fromisoformat(
                input("Enter Return Date (YYYY-MM-DD): ")
            )

            if new_return_date < new_rent_date:

                console.print(
                    "❌ Return date cannot be before rent date!",
                    style="bold red"
                )

                continue

            total_days = (
                new_return_date - new_rent_date
            ).days

            if total_days == 0:
                total_days = 1

            new_amount = float(
                input("Enter Total Amount: ")
            )

            console.print(
                "\n1. Active"
            )

            console.print(
                "2. Completed"
            )

            status_choice = input(
                "Enter Status: "
            )

            if status_choice == "1":
                new_status = "Active"

            elif status_choice == "2":
                new_status = "Completed"

            else:

                console.print(
                    "❌ Invalid Status!",
                    style="bold red"
                )

                continue

            cursor.execute(
                """
                UPDATE rental
                SET rent_date = %s,
                    return_date = %s,
                    total_days = %s,
                    total_amount = %s,
                    rental_status = %s
                WHERE rental_id = %s
                """,
                (
                    new_rent_date,
                    new_return_date,
                    total_days,
                    new_amount,
                    new_status,
                    rental_id
                )
            )

            conn.commit()

            console.print(
                "✅ All Rental Details Updated Successfully!",
                style="bold green"
            )

            show_rental(rental_id)

        # --------------------------------
        # BACK
        # --------------------------------

        elif choice == "6":

            break

        else:

            console.print(
                "❌ Invalid Choice!",
                style="bold red"
            )





def show_rental(rental_id):

    query = """
        SELECT rental_id,
               customer_id,
               vehicle_id,
               rent_date,
               return_date,
               total_days,
               total_amount,
               rental_status
        FROM rental
        WHERE rental_id = %s
    """

    cursor.execute(query, (rental_id,))
    rental = cursor.fetchone()

    if not rental:
        console.print(
            "❌ Rental Not Found!",
            style="bold red"
        )
        return

    table = Table(
        title="UPDATED RENTAL DETAILS",
        show_header=True,
        header_style="bold cyan"
    )

    table.add_column("Rental ID")
    table.add_column("Customer ID")
    table.add_column("Vehicle ID")
    table.add_column("Rent Date")
    table.add_column("Return Date")
    table.add_column("Total Days")
    table.add_column("Total Amount")
    table.add_column("Status")

    table.add_row(
        str(rental[0]),
        str(rental[1]),
        str(rental[2]),
        str(rental[3]),
        str(rental[4]),
        str(rental[5]),
        f"₹{rental[6]:.2f}",
        str(rental[7])
    )

    console.print(table)



def delete_rental():

    rental_id = int(input("Enter Rental ID: "))

    # Check whether rental exists
    cursor.execute(
        """
        SELECT rental_id, vehicle_id
        FROM rental
        WHERE rental_id = %s
        """,
        (rental_id,)
    )

    rental = cursor.fetchone()

    if not rental:

        console.print(
            "❌ Rental Not Found!",
            style="bold red"
        )

        return

    vehicle_id = rental[1]

    # Show confirmation
    console.print(
        "\n[bold yellow]Rental Found![/bold yellow]"
    )

    confirm = input(
        "Are you sure you want to delete this rental? (Y/N): "
    )

    if confirm.lower() != "y":

        console.print(
            "❌ Delete Cancelled.",
            style="bold yellow"
        )

        return

    # Delete payment associated with rental
    cursor.execute(
        """
        DELETE FROM payment
        WHERE rental_id = %s
        """,
        (rental_id,)
    )

    # Delete rental
    cursor.execute(
        """
        DELETE FROM rental
        WHERE rental_id = %s
        """,
        (rental_id,)
    )

    # Make vehicle available again
    cursor.execute(
        """
        UPDATE vehicle
        SET status = 'Available'
        WHERE vehicle_id = %s
        """,
        (vehicle_id,)
    )

    conn.commit()

    console.print(
        "\n✅ Rental Deleted Successfully!",
        style="bold green"
    )

            

            