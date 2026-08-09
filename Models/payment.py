class Payment:
    def __init__(
        self,
        rental_id,
        payment_date,
        amount,
        payment_method,
        payment_status="Pending"
    ):
        self.rental_id = rental_id
        self.payment_date = payment_date
        self.amount = amount
        self.payment_method = payment_method
        self.payment_status = payment_status