class Vehicle:

    def __init__(
        self,
        vehicle_type,
        brand,
        model,
        registration_no,
        rent_per_day,
        
        status="Available"
    ):
        self.vehicle_type = vehicle_type
        self.brand = brand
        self.model = model
        self.registration_no = registration_no
        self.rent_per_day = rent_per_day
        self.status = status