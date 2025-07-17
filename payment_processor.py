class PaymentProcessor:
    '''
    PaymentProcessor class for processing the payment including the fee.
    '''
    def __init__(self, fee_percent=2.0, max_limit=1000):
        '''
        Initialize the objects and assign the values to the data members.

        Args:
        fee_percent : Fee percentage of 2% on the amount to be process
        max_limit : Maximum amount that we can process
        '''
        self.fee_percent = fee_percent
        self.max_limit = max_limit

    def process_payment(self, amount):
        '''
        Process the payment.

        Args:
        amount : The amount that we want to process.

        Return:Total amount with fee that will be process.
        '''
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.max_limit:
            raise ValueError("Amount exceeds max limit")
        fee = (amount * self.fee_percent) / 100
        return round(amount + fee, 2)
