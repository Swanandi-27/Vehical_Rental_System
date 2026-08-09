from Services.Customer_services import *
from Services.vehicle_services import *
from Services.rental_services import *
from Services.payment_services import *
from Menus.payment_menu import *

def admin_menu():
    while True:
        print("\n1.Vehical Management\n2.Customer Management\n3.Rental Management\n4.Payment Management\n5.Exit")
        choice = int(input("enter your choice:"))
        match choice:
            case 1:
                while True:
                    print("=================Vehicle Management================")
                    print("\n1.Add Vehicle\n2.View Vehicle\n3.Update Vehicle\n4.Delete Vehicle\n5.Back")
                    ch=int(input("enter your choice:"))
                    match ch:
                        case 1:
                            add_Vehicle()
                        case 2:
                            View_vehicle()
                        case 3:
                            update_vehicle()
                        case 4:
                            delete_vehicle()
                        case 5:
                            break
                        case _:
                            print("Invalid choice")

                

            case  2:
                while True:
                    print("=============Customer Management==============")
                    print("\n1.View Customer\n2.Search Customer\n3.Update Customer\n4.Delete Customer\n5.Back")
                    ch=int(input("enter your choice:"))
                    match ch :
                        case 1:
                            view_customers()
                        case 2:
                            search_customer()
                        case 3:
                            update_customer()
                        case 4:
                            delete_customer()
                        case 5:
                            break
                        case _:
                            print("Invalid choice:")
            case 3:
                while True:
                    print("============Rental Management==============")
                    print("\n1.View all Rentals\n2.Search Rentals\n3.Update Rentals \n4.Delete Rentals\n5.Exit")
                    ip=int(input("enter your choice:"))
                    match ip:
                        case 1:
                            view_all_rental()
                        case 2:
                            search_rental()
                        case 3:
                            update_rental()
                        case 4:
                            delete_rental()
                        case 5:
                            break
                        case _:
                            print("Invalid choice")


            case 4:
                admin_payment_menu()
            
            case 5:
                break
            case _:
                print("Invalid choice")


# ===== PAYMENT MANAGEMENT =====
# 
# 1. View All Payments
# 2. Search Payment
# 3. Update Payment Status
# 4. Delete Payment
# 5. Back