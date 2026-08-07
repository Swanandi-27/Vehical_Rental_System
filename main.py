from Services.Customer_services import (
    register_customer,
    customer_login
)


def main():

    while True:

        print("""
==================================================
          VEHICLE RENTAL MANAGEMENT SYSTEM
==================================================

1. Customer Register
2. Customer Login
3. Exit

==================================================
""")

        choice = input("Enter Your Choice: ")

        if choice == "1":

            register_customer()

        elif choice == "2":

            customer_login()

        elif choice == "3":

            print("\nThank You for Using Vehicle Rental System!")
            print("Visit Again...\n")
            break

        else:

            print("\nInvalid Choice! Please Try Again.\n")


if __name__ == "__main__":
    main()