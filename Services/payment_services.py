from datetime import date
from db_conn import conn,cursor
from rich.console import Console
from rich.table import Table

console = Console()



    
def make_payment(rental_id, payment_method=None, payment_status='Paid'):
    try:
        cursor.execute("SELECT total_amount FROM rental WHERE rental_id = %s", (rental_id,))
        rental = cursor.fetchone()
        if not rental:
            console.print("[red]Error: Rental ID not found![/red]")
            return False
        amount = rental[0]  # total_amount from rental table
        today = date.today()
        if payment_status == 'Pending' or payment_method is None:
            query = """
                INSERT INTO payment (rental_id, payment_date, amount, payment_method, payment_status)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (rental_id, today, amount, None, 'Pending'))
            conn.commit()
            console.print("[yellow]Payment process cancelled. Payment status remains 'Pending'.[/yellow]")
            return True
        query = """
            INSERT INTO payment (rental_id, payment_date, amount, payment_method, payment_status)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (rental_id, today, amount, payment_method, 'Paid'))
        conn.commit()
        
        console.print(f"[green]Payment of ₹{amount} completed successfully via {payment_method}![/green]")
        return True
    except Exception as e:
        conn.rollback()
        console.print(f"[red]Payment failed: {e}[/red]")
        return False
    finally:
        cursor.close()
        conn.close()

def view_payment(rental_id):
    
    try:
        query = "SELECT * FROM payment WHERE rental_id = %s"
        cursor.execute(query, (rental_id,))
        payments = cursor.fetchall()
        if not payments:
            console.print("[yellow]No payment record found for this Rental ID.[/yellow]")
            return
        table = Table(title=f"Payment Details (Rental ID: {rental_id})")
        table.add_column("Payment ID", style="cyan")
        table.add_column("Rental ID", style="magenta")
        table.add_column("Date", style="green")
        table.add_column("Amount", style="yellow")
        table.add_column("Method", style="blue")
        table.add_column("Status", style="bold green")
        for row in payments:
           
            method_display = row[4] if row[4] else "N/A"
            table.add_row(str(row[0]), str(row[1]), str(row[2]), f"₹{row[3]}", method_display, str(row[5]))
        console.print(table)
    except Exception as e:
        console.print(f"[red]Error fetching payment details: {e}[/red]")
    finally:
        cursor.close()
        conn.close()

def payment_history(customer_id=None):
    
    try:
        if customer_id:
            query = """
                SELECT p.payment_id, p.rental_id, p.payment_date, p.amount, p.payment_method, p.payment_status
                FROM payment p
                JOIN rental r ON p.rental_id = r.rental_id
                WHERE r.customer_id = %s
            """
            cursor.execute(query, (customer_id,))
        else:
            query = """
                SELECT p.payment_id, p.rental_id, p.payment_date, p.amount, p.payment_method, p.payment_status
                FROM payment p
            """
            cursor.execute(query)
        records = cursor.fetchall()
        if not records:
            console.print("[yellow]No payment history found.[/yellow]")
            return
        table = Table(title="Payment History")
        table.add_column("Payment ID", style="cyan")
        table.add_column("Rental ID", style="magenta")
        table.add_column("Date", style="green")
        table.add_column("Amount", style="yellow")
        table.add_column("Method", style="blue")
        table.add_column("Status", style="bold green")
        for row in records:
            method_display = row[4] if row[4] else "N/A"
            table.add_row(str(row[0]), str(row[1]), str(row[2]), f"₹{row[3]}", method_display, str(row[5]))
        console.print(table)
    except Exception as e:
        console.print(f"[red]Error getting payment history: {e}[/red]")
    finally:
        cursor.close()
        conn.close()