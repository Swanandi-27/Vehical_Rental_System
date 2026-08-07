class Customer:

    def __init__(self, customer_id, customer_name, username,
                 phone, email, password, license_no, address):

        self.customer_id = customer_id
        self.customer_name = customer_name
        self.username = username
        self.phone = phone
        self.email = email
        self.password = password
        self.license_no = license_no
        self.address = address

    # Display customer details
    def display_customer(self):

        print("\n==============================")
        print("      CUSTOMER DETAILS")
        print("==============================")
        print("Customer ID   :", self.customer_id)
        print("Name          :", self.customer_name)
        print("Username      :", self.username)
        print("Phone         :", self.phone)
        print("Email         :", self.email)
        print("License No    :", self.license_no)
        print("Address       :", self.address)
        print("==============================")

    # Convert object into tuple (Useful for Insert/Update)
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

    # String representation
    def __str__(self):

        return f"""
Customer ID : {self.customer_id}
Name        : {self.customer_name}
Username    : {self.username}
Phone       : {self.phone}
Email       : {self.email}
License No  : {self.license_no}
Address     : {self.address}
"""