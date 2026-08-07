import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="vehicle_rental_system"
    )

    cursor = conn.cursor()

    print("Database Connected Successfully!")

except mysql.connector.Error as err:
    print("Database Connection Error:", err)