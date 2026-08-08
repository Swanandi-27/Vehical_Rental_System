class rental:
    def __init__(self,customer_id,vehicle_id,rent_date,return_date,total_days,total_amount,rental_status="Active"):
    
        self.customer_id = customer_id
        self.vehicle_id = vehicle_id
        self.rent_date = rent_date
        self.return_date = return_date
        self.total_days = total_days
        self.total_amount = total_amount
        self.rental_status = rental_status
   