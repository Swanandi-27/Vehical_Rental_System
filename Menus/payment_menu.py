

from SERVICES.payment_services import PaymentService
from rich.console import Console

console = Console()

def user_payment_menu(customer_id):
    while True:
        console.print("\n[bold cyan]=== USER PAYMENT MENU ===[/bold cyan]")
        console.print("1. Make Payment")
        console.print("2. View Payment Details")
        console.print("3. Payment History")
        console.print("4. Back to Dashboard")

        choice = input("Enter choice (1-4): ").strip()

        if choice == '1':
            try:
                rental_id = int(input("Enter Rental ID: "))

                console.print("\nSelect Payment Method:")
                console.print("1. Cash")
                console.print("2. UPI")
                console.print("3. Card")
                console.print("4. Cancel")
                m_choice = input("Enter choice (1-4): ").strip()

                if m_choice == '1':
                    PaymentService.make_payment(rental_id, payment_method='Cash', payment_status='Paid')
                elif m_choice == '2':
                    PaymentService.make_payment(rental_id, payment_method='UPI', payment_status='Paid')
                elif m_choice == '3':
                    PaymentService.make_payment(rental_id, payment_method='Card', payment_status='Paid')
                elif m_choice == '4':
                    PaymentService.make_payment(rental_id, payment_method=None, payment_status='Pending')
                else:
                    console.print("[red]Invalid payment method selected![/red]")

            except ValueError:
                console.print("[red]Invalid input! Please enter a valid number for Rental ID.[/red]")

        elif choice == '2':
            try:
                rental_id = int(input("Enter Rental ID: "))
                PaymentService.view_payment(rental_id)
            except ValueError:
                console.print("[red]Invalid Rental ID![/red]")

        elif choice == '3':
            PaymentService.payment_history(customer_id)

        elif choice == '4':
            break
        else:
            console.print("[red]Invalid choice, try again.[/red]")


def admin_payment_menu():
    while True:
        console.print("\n[bold magenta]=== ADMIN PAYMENT MENU ===[/bold magenta]")
        console.print("1. Make Payment")
        console.print("2. View Specific Payment Details")
        console.print("3. View All Payment History")
        console.print("4. Back to Admin Menu")
        
        choice = input("Enter choice (1-4): ").strip()

        if choice == '1':
            try:
                rental_id = int(input("Enter Rental ID: "))
                
                console.print("\nSelect Payment Method:")
                console.print("1. Cash")
                console.print("2. UPI")
                console.print("3. Card")
                console.print("4. Cancel")
                m_choice = input("Enter choice (1-4): ").strip()
                
                if m_choice == '1':
                    PaymentService.make_payment(rental_id, payment_method='Cash', payment_status='Paid')
                elif m_choice == '2':
                    PaymentService.make_payment(rental_id, payment_method='UPI', payment_status='Paid')
                elif m_choice == '3':
                    PaymentService.make_payment(rental_id, payment_method='Card', payment_status='Paid')
                elif m_choice == '4':
                    PaymentService.make_payment(rental_id, payment_method=None, payment_status='Pending')
                else:
                    console.print("[red]Invalid payment method selected![/red]")

            except ValueError:
                console.print("[red]Invalid input! Please enter a valid number for Rental ID.[/red]")

        elif choice == '2':
            try:
                rental_id = int(input("Enter Rental ID: "))
                PaymentService.view_payment(rental_id)
            except ValueError:
                console.print("[red]Invalid Rental ID![/red]")

        elif choice == '3':
            PaymentService.payment_history()

        elif choice == '4':
            break
        else:
            console.print("[red]Invalid choice, try again.[/red]")

