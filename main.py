from Services.Customer_services import (
    register_customer,
    customer_login
)
from Menus.admin_menu import *

from rich.console import Console
from rich.panel import Panel

console = Console()
AdminUname="admin"
AdminPass="123"






console.print("Welcome to the Vehicle Rental System", style="bold red")
console.print("\n1.Admin\n2.Customer\n3.Back",style="green")

choice = int(input("Enter Your choice:"))
match choice:
    case 1:
        username=input("enter username:")
        password=input("enter Password:")
        if username==AdminUname and password==AdminPass:
            console.print("✅ Login Successful!", style="bold green")
            admin_menu()
            
        else:
            console.print("❌ Invalid Username or Password", style="bold red")
    case 2: 
        print("\n1.Register\n2.Login\n3.Back")
        ch=int(input("enter yout choice:"))
        match ch:
            case  1:
                register_customer()
            case 2:
                customer_login()
            case 3:
                exit()
            case _:
                print("Invalid choice")
    case 3:
        exit()
    case _:
        print("Invalid Choice")

        
    