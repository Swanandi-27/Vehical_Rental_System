from Models.Vehicle import Vehicle 
from db_conn import conn,cursor
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def add_Vehicle():
    console.print(Panel.fit("[bold cyan]ADD VEHICLE[/bold cyan]"))
    Vehicle_type= input("Enter Vehicle Typs(Car/Bike): ")
    brand = input("Enter Brand: ")
    model=input("Enter Model: ")
    registration_no = input("Enter Registration No: ")
    rent_per_day = float(input("Enter Rent Per Day: "))
    query= """Insert into vehicle
    (vehicle_type,brand,model,registration_no,rent_per_day)
    values(%s,%s,%s,%s,%s)
    """
    values=(Vehicle_type,brand,model,registration_no,rent_per_day)
    cursor.execute(query,values)
    conn.commit()
    console.print("✅ Vehicle Added Successfully!",
        style="bold green")



def View_vehicle():
    query="select * from vehicle"
    cursor.execute(query)
    vehicles=cursor.fetchall()
    display_vehicles(vehicles)

    


def update_vehicle():
    while True:
        console.print("\n[bold cyan]======Update Customers=======[/bold cyan]")
        console.print("1.Update All Details")
        console.print("2.Update Type")
        console.print("3.Update Brand")
        console.print("4.Update Model")
        console.print("5.Update Registration No ")
        console.print("6.Update Rent/Day")
        console.print("7.Update Status")
        console.print("8.Back")
        ch=int(input("enter your choice:"))
        match ch :
            case 1:
                console.print("[cyan]=========Update All Details[/cyan]=========")
                id=int(input("Vehicle ID:"))
                query="select * from vehicle where vehicle_id =%s"
                cursor.execute(query,(id,))
                vehicle = cursor.fetchone()
                if vehicle:
                    Type=input("Enter Vehicle Typs: ")
                    Brand=input("Enter Vehicle Brand: ")
                    Model=input("Enter Vehicle Model: ")
                    Regiatration_No=input("Enter Registration NO: ")
                    Rent_Day=float(input("Enter Rent per day: "))
                    status=input("enter Vehicle status: ")

                    query="""
                        Update  vehicle
                        set vehicle_type=%s, brand=%s,
                        model=%s,registration_no=%s,rent_per_day=%s,status=%s
                        where vehicle_id=%s

                    """
                    values=(Type,Brand,Model,Regiatration_No,Rent_Day,status,id)
                    cursor.execute(query,values)
                    conn.commit()
                    console.print("✅ Vehicle Updated Successfully!", style="green")

                else:
                    console.print("❌ Vehicle  Not Found!", style="red")

            case 2:
                console.print("[cyan]=========Update Vehicle Type[/cyan]=========")
                id=int(input("Vehicle ID:"))
                vehicle_type=input("Enter Vehicle Typs: ")

                query="update vehicle set vehicle_type=%s where vehicle_id=%s"
                values=(vehicle_type,id)
                cursor.execute(query,values)
                conn.commit()
                if cursor.rowcount > 0:
                     console.print("✅ Vehicle  Type Updated Successfully!", style="bold green")
                else:
                     console.print("❌ Vehicle ID Not Found!", style="bold red")
                    

            case 3:
                console.print("[cyan]=========Update Vehicle Brand [/cyan]=========")
                id=int(input("Vehicle ID:"))
                brand=input("Enter Vehicle Brand: ")

                query="update vehicle set brand=%s where vehicle_id=%s"
                values=(brand,id)
                cursor.execute(query,values)
                conn.commit()
                if cursor.rowcount > 0:
                     console.print("✅ Vehiclee Brand Updated Successfully!", style="bold green")
                else:
                     console.print("❌ Vehicle ID Not Found!", style="bold red")
            case 4:

                console.print("[cyan]=========Update Vehicle Model[/cyan]=========")
                id=int(input("Vehicle ID:"))
                Model=input("Enter Vehicle Model: ")

                query="update vehicle set model=%s where vehicle_id=%s"
                values=(Model,id)
                cursor.execute(query,values)
                conn.commit()
                if cursor.rowcount > 0:
                     console.print("✅ Vehicle Model Updated Successfully!", style="bold green")
                else:
                     console.print("❌ Vehicel  ID Not Found!", style="bold red")

            case 5:
                console.print("[cyan]=========Update Registration NO[/cyan]=========")
                id=int(input("Vehicle ID:"))
                registration_no=input("Enter Vehicle registration_no: ")

                query="update vehicle set registration_no=%s where vehicle_id=%s"
                values=(registration_no,id)
                cursor.execute(query,values)
                conn.commit()
                if cursor.rowcount > 0:
                     console.print("✅ Vehicle Registration No Updated Successfully!", style="bold green")
                else:
                     console.print("❌ Vehicel  ID Not Found!", style="bold red")

            case 6:
                console.print("[cyan]=========Update Rent/Day[/cyan]=========")
                id=int(input("Vehicle ID:"))
                rent_day=float(input("Enter Vehicle Rent / DAY: "))

                query="update vehicle set rent_per_day=%s where vehicle_id=%s"
                values=(rent_day,id)
                cursor.execute(query,values)
                conn.commit()
                if cursor.rowcount > 0:
                     console.print("✅ Vehicle Rent per Day Updated Successfully!", style="bold green")
                else:
                     console.print("❌ Vehicel  ID Not Found!", style="bold red")

            case 7:
                console.print("[cyan]=========Update Vehicle status[/cyan]=========")
                id=int(input("Vehicle ID:"))
                status=input("Enter Vehicle Status: ")

                query="update vehicle set status=%s where vehicle_id=%s"
                values=(status,id)
                cursor.execute(query,values)
                conn.commit()
                if cursor.rowcount > 0:
                     console.print("✅ Vehicle Status  Updated Successfully!", style="bold green")
                else:
                     console.print("❌ Vehicel  ID Not Found!", style="bold red")
            case 8:
                break
            case _:
                print("Invalid choice") 


def delete_vehicle():
    id=int(input("enter vehicle id: "))
    quert="delete from vehicle where vehicle_id=%s"
    cursor.execute(quert,(id,))
    conn.commit()
    if cursor.rowcount > 0:
        console.print("✅ Vehicle Deleted  Updated Successfully!", style="bold green")
    else:
        console.print("❌ Vehicel  ID Not Found!", style="bold red")


def view_available_vehicle():
    query="""
    select vehicle_id,
    vehicle_type,
    brand,
    model,
    registration_no,
    rent_per_day
    from vehicle 
    where status = 'Available'
        """

    cursor.execute(query)
    vehicles=cursor.fetchall()
    display_vehicles(vehicles)

def Search_vehicle():  
    while True:
        print("\n1.Search vehicle by ID\n2.search vehicle by  Type\n3.search vehicle by Brand\n4.search vehicle by Model\n5.search vehicle by Rent\n6.search vehicle by status\n7.back")
        ch=int(input("enter your choice:"))
        match ch:
            case 1:
                console.print("[cyan]=========Search Vehicle By ID[/cyan]=========")
                id=int(input("enter Vehicle ID:"))
                query="select  * from vehicle where vehicle_id=%s"
                cursor.execute(query,(id,))
                vehicle = cursor.fetchall()

                display_vehicles(vehicle)

            case 2:
                console.print("[cyan]=========Search By Vehicle Type[/cyan]=========")
                vehicle_Type=input("enter Vehicle Type:")
                query="select  * from vehicle where vehicle_type=%s"
                cursor.execute(query,(vehicle_Type,))
                vehicle = cursor.fetchall()

                display_vehicles(vehicle)

            case 3:
                console.print("[cyan]=========Search By Vehicle Brand[/cyan]=========")
                brand=input("enter Vehicle Brand:")
                query="select  * from vehicle where brand=%s"
                cursor.execute(query,(brand,))
                vehicle = cursor.fetchall()

                display_vehicles(vehicle)
            case 4:
                console.print("[cyan]=========Search By Vehicle Model[/cyan]=========")
                model=input("enter Vehicle Model:")
                query="select  * from vehicle where model=%s"
                cursor.execute(query,(model,))
                vehicle = cursor.fetchall()

                display_vehicles(vehicle)

            case 5:
                console.print("[cyan]=========Search By Vehicle Rent[/cyan]=========")
                rent=int(input("enter Vehicle Rent:"))
                query="select  * from vehicle where rent_per_day=%s"
                cursor.execute(query,(rent,))
                vehicle = cursor.fetchall()

                display_vehicles(vehicle)
            case 6:
                console.print("[cyan]=========Search By Vehicle Status[/cyan]=========")
                status=input("enter Vehicle status:")
                query="select  * from vehicle where status=%s"
                cursor.execute(query,(status,))
                vehicle = cursor.fetchall()
    
                display_vehicles(vehicle)
            case 7:
                break
            case _:
                print("Invalid choice")















def display_vehicles(vehicles):

    if vehicles:

        table = Table(
            title="VEHICLE RECORDS",
            show_header=True,
            header_style="bold cyan"
        )

        table.add_column("ID", justify="center")
        table.add_column("Type")
        table.add_column("Brand")
        table.add_column("Model")
        table.add_column("Registration No")
        table.add_column("Rent/Day", justify="right")
        table.add_column("Status")

        for vehicle in vehicles:

            table.add_row(
                str(vehicle[0]),
                vehicle[1],
                vehicle[2],
                vehicle[3],
                vehicle[4],
                f"₹{vehicle[5]:.2f}",
                vehicle[6]
            )

        console.print(table)

    else:

        console.print(
            "❌ No Vehicle Found!",
            style="bold red"
        )




            
