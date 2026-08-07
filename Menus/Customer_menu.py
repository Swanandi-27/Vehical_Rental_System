from Services.Customer_services import (
    view_profile,
    update_profile,
    change_password
)


def customer_menu(customer_id):

    while True:

        print("""
==================================================
              CUSTOMER DASHBOARD
==================================================

--------------- Vehicle Services -----------------

1. View Available Vehicles
2. Search Vehicle
3. Rent Vehicle
4. Return Vehicle

--------------- Rental & Payment -----------------

5. Payment
6. View My Rentals
7. Payment History

--------------- My Account ------------------------

8. View My Profile
9. Update My Profile
10. Change Password

11. Logout

==================================================
""")

        choice = input("Enter Your Choice: ")

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
            print("\nCustomer Logout Successfully!")
            break

        
        else:
            print("\nInvalid Choice! Please Try Again.")