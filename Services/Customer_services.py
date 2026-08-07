from db_conn import conn, cursor
from Models.Customer import Customer

#Customer register 
def register_customer():

    print("\n========== CUSTOMER REGISTER ==========\n")

    name = input("Enter Customer Name : ")
    username = input("Enter Username      : ")
    phone = input("Enter Phone Number  : ")
    email = input("Enter Email         : ")
    password = input("Enter Password      : ")
    license_no = input("Enter License No    : ")
    address = input("Enter Address       : ")

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

    print("\nCustomer Registered Successfully!\n")

#customer login
def customer_login():

    print("\n========== CUSTOMER LOGIN ==========\n")

    username = input("Enter Username : ")
    password = input("Enter Password : ")

    cursor.execute("""
        SELECT customer_id
        FROM customer
        WHERE username=%s AND password=%s
    """, (username, password))

    customer = cursor.fetchone()

    if customer:

        print("\nLogin Successful!\n")

        from Menus.Customer_menu import customer_menu
        customer_menu(customer[0])

    else:

        print("\nInvalid Username or Password.\n")

#view custimer
def view_customers():

    cursor.execute("SELECT * FROM customer")

    data = cursor.fetchall()

    if not data:

        print("\nNo Customers Found.\n")
        return

    print("\n========== CUSTOMER LIST ==========\n")

    for c in data:

        customer = Customer(
            c[0], c[1], c[2], c[3],
            c[4], c[5], c[6], c[7]
        )

        customer.display_customer()
#search customer
def search_customer():

    while True:

        print("""
=============================
      SEARCH CUSTOMER
=============================

1. Search By ID
2. Search By Name
3. Search By Phone
4. Search By Email
5. Back

=============================
""")

        choice = input("Enter Choice : ")

        if choice == "1":

            cid = int(input("Enter Customer ID : "))

            cursor.execute(
                "SELECT * FROM customer WHERE customer_id=%s",
                (cid,)
            )

        elif choice == "2":

            name = input("Enter Name : ")

            cursor.execute(
                "SELECT * FROM customer WHERE customer_name=%s",
                (name,)
            )

        elif choice == "3":

            phone = input("Enter Phone : ")

            cursor.execute(
                "SELECT * FROM customer WHERE phone=%s",
                (phone,)
            )

        elif choice == "4":

            email = input("Enter Email : ")

            cursor.execute(
                "SELECT * FROM customer WHERE email=%s",
                (email,)
            )

        elif choice == "5":
            break

        else:
            print("Invalid Choice.")
            continue

        customers = cursor.fetchall()

        if customers:

            for c in customers:

                customer = Customer(
                    c[0], c[1], c[2], c[3],
                    c[4], c[5], c[6], c[7]
                )

                customer.display_customer()

        else:

            print("\nCustomer Not Found.\n")

#Update customer
def update_customer():

    cid = int(input("Enter Customer ID : "))

    cursor.execute(
        "SELECT * FROM customer WHERE customer_id=%s",
        (cid,)
    )

    data = cursor.fetchone()

    if not data:
        print("\nCustomer Not Found.\n")
        return

    while True:

        print("""
==============================
      UPDATE CUSTOMER
==============================

1. Update All Details
2. Update Name
3. Update Phone
4. Update Email
5. Update License No
6. Update Address
7. Back

==============================
""")

        choice = input("Enter Choice : ")

        if choice == "1":

            name = input("Enter Name : ")
            phone = input("Enter Phone : ")
            email = input("Enter Email : ")
            license_no = input("Enter License No : ")
            address = input("Enter Address : ")

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

            print("\nCustomer Updated Successfully!\n")

        elif choice == "2":

            name = input("Enter New Name : ")

            cursor.execute("""
                UPDATE customer
                SET customer_name=%s
                WHERE customer_id=%s
            """, (name, cid))

            conn.commit()

            print("\nName Updated Successfully!\n")

        elif choice == "3":

            phone = input("Enter New Phone : ")

            cursor.execute("""
                UPDATE customer
                SET phone=%s
                WHERE customer_id=%s
            """, (phone, cid))

            conn.commit()

            print("\nPhone Updated Successfully!\n")

        elif choice == "4":

            email = input("Enter New Email : ")

            cursor.execute("""
                UPDATE customer
                SET email=%s
                WHERE customer_id=%s
            """, (email, cid))

            conn.commit()

            print("\nEmail Updated Successfully!\n")

        elif choice == "5":

            license_no = input("Enter New License No : ")

            cursor.execute("""
                UPDATE customer
                SET license_no=%s
                WHERE customer_id=%s
            """, (license_no, cid))

            conn.commit()

            print("\nLicense Updated Successfully!\n")

        elif choice == "6":

            address = input("Enter New Address : ")

            cursor.execute("""
                UPDATE customer
                SET address=%s
                WHERE customer_id=%s
            """, (address, cid))

            conn.commit()

            print("\nAddress Updated Successfully!\n")

        elif choice == "7":
            break

        else:
            print("\nInvalid Choice!\n")

#Delete customer
def delete_customer():

    cid = int(input("Enter Customer ID : "))

    cursor.execute(
        "SELECT * FROM customer WHERE customer_id=%s",
        (cid,)
    )

    data = cursor.fetchone()

    if not data:
        print("\nCustomer Not Found.\n")
        return

    confirm = input("Are you sure you want to delete this customer? (Y/N): ")

    if confirm.lower() == "y":

        cursor.execute(
            "DELETE FROM customer WHERE customer_id=%s",
            (cid,)
        )

        conn.commit()

        print("\nCustomer Deleted Successfully!\n")

    else:

        print("\nDelete Cancelled.\n")

#view profile
def view_profile(customer_id):

    cursor.execute("""
        SELECT *
        FROM customer
        WHERE customer_id=%s
    """, (customer_id,))

    data = cursor.fetchone()

    if data:

        customer = Customer(
            data[0], data[1], data[2], data[3],
            data[4], data[5], data[6], data[7]
        )

        customer.display_customer()

    else:

        print("\nProfile Not Found.\n")

#Update profile
def update_profile(customer_id):

    while True:

        print("""
==============================
      UPDATE PROFILE
==============================

1. Update Name
2. Update Phone
3. Update Email
4. Update License No
5. Update Address
6. Back

==============================
""")

        choice = input("Enter Choice : ")

        if choice == "1":

            name = input("Enter New Name : ")

            cursor.execute("""
                UPDATE customer
                SET customer_name=%s
                WHERE customer_id=%s
            """, (name, customer_id))

            conn.commit()

            print("\nName Updated Successfully!\n")

        elif choice == "2":

            phone = input("Enter New Phone : ")

            cursor.execute("""
                UPDATE customer
                SET phone=%s
                WHERE customer_id=%s
            """, (phone, customer_id))

            conn.commit()

            print("\nPhone Updated Successfully!\n")

        elif choice == "3":

            email = input("Enter New Email : ")

            cursor.execute("""
                UPDATE customer
                SET email=%s
                WHERE customer_id=%s
            """, (email, customer_id))

            conn.commit()

            print("\nEmail Updated Successfully!\n")

        elif choice == "4":

            license_no = input("Enter New License No : ")

            cursor.execute("""
                UPDATE customer
                SET license_no=%s
                WHERE customer_id=%s
            """, (license_no, customer_id))

            conn.commit()

            print("\nLicense Number Updated Successfully!\n")

        elif choice == "5":

            address = input("Enter New Address : ")

            cursor.execute("""
                UPDATE customer
                SET address=%s
                WHERE customer_id=%s
            """, (address, customer_id))

            conn.commit()

            print("\nAddress Updated Successfully!\n")

        elif choice == "6":
            break

        else:
            print("\nInvalid Choice!\n")

#change password
def change_password(customer_id):

    cursor.execute(
        "SELECT password FROM customer WHERE customer_id=%s",
        (customer_id,)
    )

    data = cursor.fetchone()

    if not data:
        print("\nCustomer Not Found.\n")
        return

    current_password = input("Enter Current Password : ")

    if current_password != data[0]:
        print("\nCurrent Password is Incorrect.\n")
        return

    new_password = input("Enter New Password : ")

    confirm_password = input("Confirm New Password : ")

    if new_password != confirm_password:
        print("\nPasswords do not match.\n")
        return

    cursor.execute("""
        UPDATE customer
        SET password=%s
        WHERE customer_id=%s
    """, (new_password, customer_id))

    conn.commit()

    print("\nPassword Changed Successfully!\n")