# 🚗 Vehicle Rental System

A **console-based Vehicle Rental System** developed using **Python and MySQL**.
The system allows administrators to manage vehicles, customers, rentals, and payments, while customers can register, log in, search for vehicles, rent/return vehicles, and view their rental history.

---

## 📌 Project Overview

The Vehicle Rental System is designed to simplify the process of renting and managing vehicles.

The application provides two types of users:

* 👨‍💼 **Admin**
* 👤 **Customer**

The Admin can manage vehicles, customers, rentals, and generate reports, while customers can browse available vehicles and manage their rentals.

---

## 🎯 Objectives

* Automate the vehicle rental process.
* Maintain customer and vehicle information in a database.
* Allow customers to easily rent and return vehicles.
* Track rental dates, duration, and total rental amount.
* Provide administrators with complete control over the system.
* Reduce manual record keeping and improve data management.

---

## 🛠️ Technologies Used

| Technology         | Purpose                           |
| ------------------ | --------------------------------- |
| 🐍 Python          | Application development           |
| 🗄️ MySQL          | Database management               |
| 🎨 Rich            | Console UI and formatted tables   |
| 🔗 MySQL Connector | Python-MySQL database connection  |
| 🐙 Git & GitHub    | Version control and collaboration |

---

## ✨ Features

### 👨‍💼 Admin Features

* 🔐 Admin Login
* 🚗 Add Vehicle
* 👀 View Vehicles
* ✏️ Update Vehicle
* 🗑️ Delete Vehicle
* 👤 View Customers
* ✏️ Update Customer Details
* 🗑️ Delete Customer
* 📋 View Rental Records
* 💳 Manage Payments
* 📊 Generate Reports

### 👤 Customer Features

* 📝 Customer Registration
* 🔐 Customer Login
* 🚘 View Available Vehicles
* 🔎 Search Vehicles
* 🚗 Rent Vehicle
* 🔄 Return Vehicle
* 📋 View My Rentals
* 👤 View My Profile
* 🔑 Change Password
* 🚪 Logout

---

## 🏗️ Project Structure

```text
Vehicle_Rental_System/
│
├── main.py
├── db_conn.py
├── create_tables.sql
│
├── Models/
│   ├── Customer.py
│   └── Vehicle.py
|   |__rental.py
|   |__payment.py 
│
├── Menus/
│   ├── admin_menu.py
│   ├── customer_menu.py
│   └──payment_menu.py
│
├── services/
│   ├── customer_services.py
│   ├── vehicle_services.py
│   ├── rental_services.py
│   ├── payment_services.py
│   
│
└── README.md
```

> The exact folder/file names may vary depending on the final project structure.

---

## 🗄️ Database Design

The system uses **MySQL** to store and manage application data.

### Main Tables

#### 👤 Customer

Stores customer information.

```text
customer
├── customer_id
├── customer_name
├── phone
├── email
├── password
├── license_no
└── address
```

#### 🚗 Vehicle

Stores vehicle details.

```text
vehicle
├── vehicle_id
├── vehicle_type
├── brand
├── model
├── registration_no
├── rent_per_day
└── status
```

#### 📋 Rental

Stores rental transactions.

```text
rental
├── rental_id
├── customer_id
├── vehicle_id
├── rent_date
├── return_date
├── total_days
├── total_amount
└── rental_status
```

#### 💳 Payment

Stores payment information.

```text
payment
├── payment_id
├── rental_id
├── payment_date
├── amount
├── payment_method
└── payment_status
```



## ⚙️ How the System Works

### 1️⃣ Start Application

The user runs:

```bash
python main.py
```

### 2️⃣ Select User Type

The system provides options for:

```text
1. Admin
2. Customer
3. Exit
```

### 3️⃣ Admin Workflow

```text
Admin Login
     ↓
Admin Dashboard
     ↓
Vehicle Management
Customer Management
Rental Management
Payment Management
Reports
```

### 4️⃣ Customer Workflow

```text
Customer Registration/Login
           ↓
    Customer Dashboard
           ↓
 ┌──────────────────────┐
 │ View Vehicles        │
 │ Search Vehicle       │
 │ Rent Vehicle         │
 │ Return Vehicle       │
 │ View My Rentals      │
 │ My Profile           │
 └──────────────────────┘
```

---

## 🚗 Vehicle Rental Process

1. Customer logs into the system.
2. Customer views available vehicles.
3. Customer selects a vehicle.
4. Customer enters the rental date and return date.
5. System calculates the rental duration.
6. Total rental amount is calculated based on the daily rent.
7. Rental record is stored in MySQL.
8. Vehicle status is changed from **Available** to **Rented**.

### Example Calculation

```text
Total Days = Return Date - Rent Date

Total Amount = Total Days × Rent Per Day
```

---

## 🔄 Vehicle Return Process

When a customer returns a vehicle:

```text
Customer
   ↓
Return Vehicle
   ↓
Find Active Rental
   ↓
Update Rental Status
   ↓
Update Vehicle Status
   ↓
Vehicle becomes Available
```

---

## 🎨 Console Interface

The project uses the **Rich Python library** to create a better console experience.

It includes:

* Colored messages
* Panels
* Tables
* Success/error indicators
* Formatted menus

